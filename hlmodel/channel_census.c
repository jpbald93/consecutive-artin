/*
 * channel_census.c — Paper 6: joint residue-channel census for consecutive-prime
 * Artin correlations.
 *
 * For each consecutive prime pair (p, p') with gap g = p' - p, and each base a in
 * BASES, accumulate a 2x2 Artin joint count in the channel
 *      (r = p mod M_a,  gap-index = g/2)
 * where M_a = lcm(disc Q(sqrt(sqfree(a))), 840).
 *
 * Output: one binary file per base: header (M, GMAX slots) then uint32 counts
 * cnt[r][gidx][4] with 4 = (a00,a01,a10,a11), aXY = (artin_p==X, artin_p'==Y).
 * gidx = g/2 - 1 for g in [2,300], clamped to last slot for g>300 (max prime gap
 * below 1e9 is 282, so no clamping actually occurs).
 *
 * Compile: gcc -O3 -o channel_census channel_census.c -lm
 * Usage:   ./channel_census <limit> <outdir>
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define SEG_SIZE   (1 << 22)
#define SMALL_LIM  100000
#define NGAP       150   /* g = 2,4,...,300 */

static const int BASES[] = {2, 3, 5, 6, 7, 10, 11, 13, 15, 17, 21, 29};
static const long MODS[] = {840,840,840,840,840,840,9240,10920,840,14280,840,24360};
#define NB (int)(sizeof(BASES)/sizeof(BASES[0]))

static char small_composite[SMALL_LIM + 1];
static long small_primes[10000];
static int  n_small = 0;

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

static uint32_t *cnt[NB];
static long joint[NB][2][2];
static long n_pairs = 0;

int main(int argc, char **argv) {
    long LIMIT = (argc > 1) ? atol(argv[1]) : 1000000000L;
    const char *outdir = (argc > 2) ? argv[2] : ".";

    build_small();
    for (int b = 0; b < NB; b++) {
        cnt[b] = calloc((size_t)MODS[b] * NGAP * 4, sizeof(uint32_t));
        if (!cnt[b]) { fprintf(stderr, "oom base %d\n", BASES[b]); return 1; }
    }
    memset(joint, 0, sizeof joint);

    char *seg = malloc(SEG_SIZE);
    long prev_p = 0;
    int  prev_art[NB]; memset(prev_art, 0, sizeof prev_art);
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
            if (p < 5) continue;

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
                long gi = g / 2 - 1;
                if (gi >= NGAP) gi = NGAP - 1;
                n_pairs++;
                for (int b = 0; b < NB; b++) {
                    long r = prev_p % MODS[b];
                    cnt[b][((size_t)r * NGAP + gi) * 4 + (prev_art[b] * 2 + art[b])]++;
                    joint[b][prev_art[b]][art[b]]++;
                }
            }
            prev_p = p;
            memcpy(prev_art, art, sizeof art);
            if (++count % 2000000 == 0) {
                fprintf(stderr, "  p=%ld primes=%ld pairs=%ld\n", p, count, n_pairs);
                fflush(stderr);
            }
        }
    }

    char path[512];
    for (int b = 0; b < NB; b++) {
        snprintf(path, sizeof path, "%s/channels_%d.bin", outdir, BASES[b]);
        FILE *f = fopen(path, "wb");
        int64_t hdr[4] = {BASES[b], MODS[b], NGAP, n_pairs};
        fwrite(hdr, sizeof(int64_t), 4, f);
        fwrite(cnt[b], sizeof(uint32_t), (size_t)MODS[b] * NGAP * 4, f);
        fclose(f);
    }
    snprintf(path, sizeof path, "%s/joint_summary.json", outdir);
    FILE *f = fopen(path, "w");
    fprintf(f, "{\n  \"limit\": %ld,\n  \"n_pairs\": %ld,\n  \"bases\": {\n", LIMIT, n_pairs);
    for (int b = 0; b < NB; b++)
        fprintf(f, "    \"%d\": [[%ld,%ld],[%ld,%ld]]%s\n", BASES[b],
                joint[b][0][0], joint[b][0][1], joint[b][1][0], joint[b][1][1],
                b == NB - 1 ? "" : ",");
    fprintf(f, "  }\n}\n");
    fclose(f);
    fprintf(stderr, "DONE primes=%ld pairs=%ld\n", count, n_pairs);
    return 0;
}
