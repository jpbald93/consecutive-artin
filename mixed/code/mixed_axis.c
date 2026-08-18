/*
 * mixed_axis.c — PAPER 4: cross-base correlation of CONSECUTIVE primes.
 *
 * For each consecutive prime pair (p_n, p_{n+1}) and each ORDERED base pair
 * (a, b), accumulate the 2x2 joint counts of
 *      ( 1[p_n Artin base a],  1[p_{n+1} Artin base b] ).
 * Diagonal (a == b) reproduces papers 1-2; off-diagonal is new.
 *
 * Also per-gap tables (g <= GAP_MAX) for the MIXED EXCLUSION LAW test:
 * classification of gap classes where chi_a at p and chi_b at p+g are jointly
 * forced so that (a Artin p) and (b Artin p+g) cannot both hold.
 *
 * Memory: 12*12*301*4 longs ~ 1.4 MB. Fine.
 *
 * gcc -O3 -o mixed_axis mixed_axis.c -lm
 * ./mixed_axis <limit> <out.json>
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SEG_SIZE   (1 << 22)
#define SMALL_LIM  100000
#define GAP_MAX    300

static const int BASES[] = {2, 3, 5, 6, 7, 10, 11, 13, 15, 17, 21, 29};
#define NB (int)(sizeof(BASES)/sizeof(BASES[0]))

static char  small_composite[SMALL_LIM + 1];
static long  small_primes[10000];
static int   n_small = 0;

static void build_small(void) {
    for (long i = 2; i <= SMALL_LIM; i++)
        if (!small_composite[i]) {
            small_primes[n_small++] = i;
            for (long j = i * i; j <= SMALL_LIM; j += i) small_composite[j] = 1;
        }
}

static long powmod(long b, long e, long m) {
    long r = 1; b %= m; if (b < 0) b += m;
    while (e > 0) {
        if (e & 1) r = (long)(((__int128)r * b) % m);
        b = (long)(((__int128)b * b) % m);
        e >>= 1;
    }
    return r;
}

/* joint[a][b][i][j]: i = Artin_a(p_n), j = Artin_b(p_{n+1}) */
static long joint[NB][NB][2][2];
/* gapjoint[a][b][g][i][j] */
static long (*gapjoint)[NB][GAP_MAX + 1][2][2];
static long n_pairs = 0;

int main(int argc, char **argv) {
    long LIMIT = (argc > 1) ? atol(argv[1]) : 1000000000L;
    const char *out = (argc > 2) ? argv[2] : "mixed_axis.json";

    build_small();
    memset(joint, 0, sizeof joint);
    gapjoint = calloc(NB, sizeof *gapjoint);
    if (!gapjoint) { fprintf(stderr, "oom\n"); return 1; }

    char *seg = malloc(SEG_SIZE);
    if (!seg) { fprintf(stderr, "oom\n"); return 1; }

    long prev_p = 0;
    int  prev_art[NB];
    memset(prev_art, 0, sizeof prev_art);
    long count = 0;

    for (long lo = 2; lo <= LIMIT; lo += SEG_SIZE) {
        long hi = lo + SEG_SIZE - 1;
        if (hi > LIMIT) hi = LIMIT;
        memset(seg, 0, SEG_SIZE);
        for (int i = 0; i < n_small; i++) {
            long q = small_primes[i];
            if (q * q > hi) break;
            long start = (lo + q - 1) / q * q;
            if (start < q * q) start = q * q;
            for (long j = start; j <= hi; j += q) seg[j - lo] = 1;
        }
        for (long n = lo; n <= hi; n++) {
            if (seg[n - lo]) continue;
            long p = n;
            if (p < 5) continue;   /* skip 2, 3; smallest base prime issues */

            long pm1 = p - 1, tmp = pm1, fac[64]; int nf = 0;
            for (int i = 0; i < n_small; i++) {
                long d = small_primes[i];
                if (d * d > tmp) break;
                if (tmp % d == 0) { fac[nf++] = d; while (tmp % d == 0) tmp /= d; }
            }
            if (tmp > 1) fac[nf++] = tmp;

            int art[NB];
            for (int b = 0; b < NB; b++) {
                long a = BASES[b];
                if (a % p == 0) { art[b] = 0; continue; }
                int ok = 1;
                for (int i = 0; i < nf && ok; i++)
                    if (powmod(a, pm1 / fac[i], p) == 1) ok = 0;
                art[b] = ok;
            }

            if (prev_p) {
                long g = p - prev_p;
                n_pairs++;
                for (int a = 0; a < NB; a++)
                    for (int b = 0; b < NB; b++) {
                        joint[a][b][prev_art[a]][art[b]]++;
                        if (g <= GAP_MAX)
                            gapjoint[a][b][g][prev_art[a]][art[b]]++;
                    }
            }
            prev_p = p;
            memcpy(prev_art, art, sizeof art);

            if (++count % 2000000 == 0) {
                fprintf(stderr, "  p=%ld primes=%ld\n", p, count);
                fflush(stderr);
            }
        }
    }

    FILE *f = fopen(out, "w");
    fprintf(f, "{\n\"limit\": %ld,\n\"n_pairs\": %ld,\n\"bases\": [", LIMIT, n_pairs);
    for (int b = 0; b < NB; b++) fprintf(f, "%d%s", BASES[b], b < NB-1 ? "," : "");
    fprintf(f, "],\n\"joint\": {\n");
    for (int a = 0; a < NB; a++)
        for (int b = 0; b < NB; b++) {
            fprintf(f, "  \"%d,%d\": [[%ld,%ld],[%ld,%ld]]%s\n",
                    BASES[a], BASES[b],
                    joint[a][b][0][0], joint[a][b][0][1],
                    joint[a][b][1][0], joint[a][b][1][1],
                    (a == NB-1 && b == NB-1) ? "" : ",");
        }
    fprintf(f, "},\n\"gap\": {\n");
    int firstpair = 1;
    for (int a = 0; a < NB; a++)
        for (int b = 0; b < NB; b++) {
            if (!firstpair) fprintf(f, ",\n");
            firstpair = 0;
            fprintf(f, "  \"%d,%d\": {", BASES[a], BASES[b]);
            int first = 1;
            for (int g = 2; g <= GAP_MAX; g++) {
                long t = gapjoint[a][b][g][0][0] + gapjoint[a][b][g][0][1]
                       + gapjoint[a][b][g][1][0] + gapjoint[a][b][g][1][1];
                if (!t) continue;
                if (!first) fprintf(f, ",");
                fprintf(f, "\"%d\":[[%ld,%ld],[%ld,%ld]]", g,
                        gapjoint[a][b][g][0][0], gapjoint[a][b][g][0][1],
                        gapjoint[a][b][g][1][0], gapjoint[a][b][g][1][1]);
                first = 0;
            }
            fprintf(f, "}");
        }
    fprintf(f, "\n}\n}\n");
    fclose(f);
    fprintf(stderr, "DONE primes=%ld pairs=%ld -> %s\n", count, n_pairs, out);
    return 0;
}
