/*
 * layers.c — Paper 7: layer decomposition of consecutive-prime Artin correlation.
 *
 * For consecutive primes (p,q) and each base a, each layer ell in {3,5,7,11,13}:
 *   binding[ell]:  2x2 counts of (ell | p-1, ell | q-1)                (base-free)
 *   symbol[ell][a]: 2x2 counts of (a^((p-1)/ell)==1, a^((q-1)/ell)==1)
 *                   restricted to pairs where BOTH bind
 *   quad[a]:       2x2 counts of (chi_a(p)=+1, chi_a(q)=+1)  via Euler criterion
 *                   (the ell=2 layer ALWAYS binds)
 *   artin[a]:      2x2 counts of Artin status (for the reconstruction check)
 *
 * gcc -O3 -o layers layers.c -lm     ; ./layers <limit> <out.json>
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SEG_SIZE  (1 << 22)
#define SMALL_LIM 100000

static const int BASES[] = {2, 3, 5, 6, 7, 10, 11, 13, 15};
#define NB (int)(sizeof(BASES)/sizeof(BASES[0]))
static const int SQF[]   = {2, 3, 5, 6, 7, 10, 11, 13, 15};
static const int ELLS[]  = {3, 5, 7, 11, 13};
#define NL (int)(sizeof(ELLS)/sizeof(ELLS[0]))

static char small_composite[SMALL_LIM + 1];
static long small_primes[10000];
static int  n_small = 0;

static void build_small(void) {
    for (long i = 2; i <= SMALL_LIM; i++)
        if (!small_composite[i]) {
            small_primes[n_small++] = i;
            for (long j = i*i; j <= SMALL_LIM; j += i) small_composite[j] = 1;
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

static long bindtab[NL][2][2];
static long symtab[NL][NB][2][2];
static long quadtab[NB][2][2];
static long arttab[NB][2][2];
static long n_pairs = 0;

int main(int argc, char **argv) {
    long LIMIT = (argc > 1) ? atol(argv[1]) : 1000000000L;
    const char *out = (argc > 2) ? argv[2] : "layers_1e9.json";
    build_small();

    char *seg = malloc(SEG_SIZE);
    long prev_p = 0;
    int  prev_bind[NL], prev_sym[NL][NB], prev_quad[NB], prev_art[NB];
    long count = 0;

    for (long lo = 2; lo <= LIMIT; lo += SEG_SIZE) {
        long hi = lo + SEG_SIZE - 1; if (hi > LIMIT) hi = LIMIT;
        memset(seg, 0, SEG_SIZE);
        for (int i = 0; i < n_small; i++) {
            long q = small_primes[i]; if (q*q > hi) break;
            long st = (lo + q - 1)/q*q; if (st < q*q) st = q*q;
            for (long j = st; j <= hi; j += q) seg[j-lo] = 1;
        }
        for (long n = lo; n <= hi; n++) {
            if (seg[n-lo]) continue;
            long p = n; if (p < 17) continue;   /* skip primes dividing any base */

            long pm1 = p-1, tmp = pm1, fac[64]; int nf = 0;
            for (int i = 0; i < n_small; i++) {
                long dd = small_primes[i]; if (dd*dd > tmp) break;
                if (tmp % dd == 0) { fac[nf++] = dd; while (tmp % dd == 0) tmp /= dd; }
            }
            if (tmp > 1) fac[nf++] = tmp;

            int bindv[NL], symv[NL][NB], quadv[NB], artv[NB];
            for (int l = 0; l < NL; l++) {
                bindv[l] = (pm1 % ELLS[l] == 0);
                for (int b = 0; b < NB; b++) symv[l][b] = -1;
                if (bindv[l])
                    for (int b = 0; b < NB; b++)
                        symv[l][b] = (powmod(BASES[b], pm1/ELLS[l], p) == 1);
            }
            for (int b = 0; b < NB; b++) {
                quadv[b] = (powmod(SQF[b], pm1/2, p) == 1);   /* chi=+1? */
                int ok = 1;
                for (int i = 0; i < nf && ok; i++)
                    if (powmod(BASES[b], pm1/fac[i], p) == 1) ok = 0;
                artv[b] = ok;
            }

            if (prev_p) {
                n_pairs++;
                for (int l = 0; l < NL; l++) {
                    bindtab[l][prev_bind[l]][bindv[l]]++;
                    if (prev_bind[l] && bindv[l])
                        for (int b = 0; b < NB; b++)
                            symtab[l][b][prev_sym[l][b]][symv[l][b]]++;
                }
                for (int b = 0; b < NB; b++) {
                    quadtab[b][prev_quad[b]][quadv[b]]++;
                    arttab[b][prev_art[b]][artv[b]]++;
                }
            }
            prev_p = p;
            memcpy(prev_bind, bindv, sizeof bindv);
            memcpy(prev_sym, symv, sizeof symv);
            memcpy(prev_quad, quadv, sizeof quadv);
            memcpy(prev_art, artv, sizeof artv);
            if (++count % 2000000 == 0) { fprintf(stderr,"  p=%ld n=%ld\n",p,count); fflush(stderr); }
        }
    }

    FILE *f = fopen(out, "w");
    fprintf(f, "{\n \"limit\": %ld,\n \"n_pairs\": %ld,\n \"bases\": [", LIMIT, n_pairs);
    for (int b = 0; b < NB; b++) fprintf(f, "%d%s", BASES[b], b==NB-1?"":",");
    fprintf(f, "],\n \"ells\": [");
    for (int l = 0; l < NL; l++) fprintf(f, "%d%s", ELLS[l], l==NL-1?"":",");
    fprintf(f, "],\n \"bind\": {");
    for (int l = 0; l < NL; l++)
        fprintf(f, "\"%d\": [[%ld,%ld],[%ld,%ld]]%s", ELLS[l],
            bindtab[l][0][0],bindtab[l][0][1],bindtab[l][1][0],bindtab[l][1][1],
            l==NL-1?"":", ");
    fprintf(f, "},\n \"sym\": {");
    for (int l = 0; l < NL; l++) {
        fprintf(f, "\"%d\": {", ELLS[l]);
        for (int b = 0; b < NB; b++)
            fprintf(f, "\"%d\": [[%ld,%ld],[%ld,%ld]]%s", BASES[b],
                symtab[l][b][0][0],symtab[l][b][0][1],symtab[l][b][1][0],symtab[l][b][1][1],
                b==NB-1?"":", ");
        fprintf(f, "}%s", l==NL-1?"":", ");
    }
    fprintf(f, "},\n \"quad\": {");
    for (int b = 0; b < NB; b++)
        fprintf(f, "\"%d\": [[%ld,%ld],[%ld,%ld]]%s", BASES[b],
            quadtab[b][0][0],quadtab[b][0][1],quadtab[b][1][0],quadtab[b][1][1],
            b==NB-1?"":", ");
    fprintf(f, "},\n \"artin\": {");
    for (int b = 0; b < NB; b++)
        fprintf(f, "\"%d\": [[%ld,%ld],[%ld,%ld]]%s", BASES[b],
            arttab[b][0][0],arttab[b][0][1],arttab[b][1][0],arttab[b][1][1],
            b==NB-1?"":", ");
    fprintf(f, "}\n}\n");
    fclose(f);
    fprintf(stderr, "DONE pairs=%ld -> %s\n", n_pairs, out);
    return 0;
}
