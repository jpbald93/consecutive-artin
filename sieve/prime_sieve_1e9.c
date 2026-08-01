/*
 * prime_sieve_1e9.c  —  segmented sieve for 10^9
 * Uses a segmented Eratosthenes to avoid allocating 1GB of RAM at once.
 * Segment size: 2^21 ≈ 2M bytes per block.
 *
 * Compile:
 *   gcc -O3 -I/usr/include/x86_64-linux-gnu -o prime_sieve_1e9 prime_sieve_1e9.c -lm -lgmp
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <gmp.h>

#define LIMIT      1000000000L   /* 10^9 */
#define SEG_SIZE   (1 << 21)     /* ~2M per segment */

/* ── tiny sieve for primes up to sqrt(LIMIT) ≈ 31623 ── */
#define SMALL_LIM  32000
static char small_composite[SMALL_LIM + 1];
static long small_primes[3500];
static int  n_small = 0;

void build_small(void) {
    for (long i = 2; i <= SMALL_LIM; i++) {
        if (!small_composite[i]) {
            small_primes[n_small++] = i;
            for (long j = i*i; j <= SMALL_LIM; j += i)
                small_composite[j] = 1;
        }
    }
}

/* ── omega(m): distinct prime factors by trial division ── */
int omega(long m) {
    int c = 0;
    for (long d = 2; d * d <= m; d++) {
        if (m % d == 0) { c++; while (m % d == 0) m /= d; }
    }
    return c + (m > 1);
}

/* ── Artin check: is 10 a primitive root mod p? ── */
int is_artin10(long p) {
    long pm1 = p - 1, tmp = pm1;
    long fac[64]; int nf = 0;
    for (long d = 2; d * d <= tmp; d++) {
        if (tmp % d == 0) { fac[nf++] = d; while (tmp % d == 0) tmp /= d; }
    }
    if (tmp > 1) fac[nf++] = tmp;

    mpz_t base, mod, exp, res;
    mpz_inits(base, mod, exp, res, NULL);
    mpz_set_si(base, 10);
    mpz_set_si(mod, p);

    int ok = 1;
    for (int i = 0; i < nf && ok; i++) {
        mpz_set_si(exp, pm1 / fac[i]);
        mpz_powm(res, base, exp, mod);
        if (mpz_cmp_si(res, 1) == 0) ok = 0;
    }
    mpz_clears(base, mod, exp, res, NULL);
    return ok;
}

int main(void) {
    build_small();
    fprintf(stderr, "Small primes built: %d primes up to %d\n", n_small, SMALL_LIM);

    static char seg[SEG_SIZE];

    /* track previous prime for gap calculation */
    long prev_prime = 5;   /* we start output from p=7 */
    long prev_prev  = 3;

    /* We need to buffer one prime ahead to get next_gap.
       Strategy: process segment, collect primes, then emit all but last,
       carrying last into next segment. */

    long *buf = malloc(200000 * sizeof(long));  /* plenty for one segment */
    long buf_n = 0;
    long carry_prime = 7;   /* first prime we'll emit */

    /* prime at very start — we need: prev of 7 is 5, prev of 5 is 3 */
    /* We handle 7 specially after the loop */

    printf("p,prev_gap,next_gap,min_gap,loneliness,omega_pm1,is_artin10,pmod4,pmod8,pmod12\n");
    fflush(stdout);

    /* ── segmented sieve ── */
    for (long low = 2; low <= LIMIT; low += SEG_SIZE) {
        long high = low + SEG_SIZE - 1;
        if (high > LIMIT) high = LIMIT;
        long len = high - low + 1;

        memset(seg, 0, len);

        /* sieve this segment */
        for (int i = 0; i < n_small; i++) {
            long sp = small_primes[i];
            long start = ((low + sp - 1) / sp) * sp;
            if (start == sp) start += sp;
            for (long j = start; j <= high; j += sp)
                seg[j - low] = 1;
        }
        if (low == 2) { seg[0] = 1; seg[1] = 0; /* 2 is prime */ }

        /* collect primes in this segment into buf */
        buf_n = 0;
        for (long i = (low < 7 ? 7 - low : 0); i < len; i++) {
            long p = low + i;
            if (!seg[i] && p >= 7)
                buf[buf_n++] = p;
        }

        /* emit: we need carry_prime's next_gap = buf[0] - carry_prime (if buf_n>0)
           We already have prev_prime from the previous iteration. */
        if (buf_n > 0) {
            /* emit carry_prime if it's >= 7 */
            if (carry_prime >= 7) {
                long p        = carry_prime;
                long pg       = p - prev_prime;
                long ng       = buf[0] - p;
                long mg       = pg < ng ? pg : ng;
                double L      = (double)mg / log((double)p);
                int   om      = omega(p - 1);
                int   artin   = is_artin10(p);
                printf("%ld,%ld,%ld,%ld,%.6f,%d,%d,%ld,%ld,%ld\n",
                       p, pg, ng, mg, L, om, artin,
                       p%4, p%8, p%12);
            }
            prev_prime = carry_prime;

            /* emit buf[0] .. buf[buf_n-2] */
            for (long k = 0; k < buf_n - 1; k++) {
                long p  = buf[k];
                long pg = p - prev_prime;
                long ng = buf[k+1] - p;
                long mg = pg < ng ? pg : ng;
                double L = (double)mg / log((double)p);
                int  om    = omega(p - 1);
                int  artin = is_artin10(p);
                printf("%ld,%ld,%ld,%ld,%.6f,%d,%d,%ld,%ld,%ld\n",
                       p, pg, ng, mg, L, om, artin,
                       p%4, p%8, p%12);
                prev_prime = p;
            }
            carry_prime = buf[buf_n - 1];
        }
        if (low % 50000000 == 0 || low == 2)
            fprintf(stderr, "  processed up to %ld ...\n", high);
    }
    /* last prime in dataset — can't compute next_gap; skip it */
    fprintf(stderr, "Done.\n");
    free(buf);
    return 0;
}
