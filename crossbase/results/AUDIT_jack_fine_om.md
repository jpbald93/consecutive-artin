# jack audit: `crossbase_fine` and `crossbase_om` at 10⁹ — 2026-09-11

## Verdict: PASS — both outputs byte-identical to the shipped results

These were the two Paper 3 computations not previously re-run independently.
Table 8's model comparison rests on `crossbase_fine_1e9.json`, so it was the
more important of the two.

## Method

Sources were fetched **from the public repository**, not copied from this
workspace — this simultaneously tests the reproduction route a referee would
actually use:

```
git clone --depth 1 https://github.com/jpbald93/consecutive-artin.git
# HEAD: 5ccd9b2 "Paper 2: build the submission set (was missing entirely)"
crossbase/code/crossbase_fine.c   sha256 0aca8d80…  matches local copy exactly
crossbase/code/crossbase_om.c     sha256 5661c0b4…  differs from local (see note)
```

Compiled `gcc -O3 -march=native` on jack (AMD Ryzen AI MAX+ 395, 32 cores,
gcc 15.2.0) and run at limit 10⁹.

## Result

| output | jack md5 | shipped md5 | match |
|---|---|---|---|
| `crossbase_fine_1e9.json` | `6d5d2c8d4a2f80f7d508bc0c4a86180a` | `6d5d2c8d4a2f80f7d508bc0c4a86180a` | **byte-identical** |
| `crossbase_om_1e9.json` | `f1acfc1680a448f4f54d943fbdf569e2` | `f1acfc1680a448f4f54d943fbdf569e2` | **byte-identical** |

Both report `n_primes = 50,847,532`, matching the shipped files and consistent
with π(10⁹) = 50,847,534 minus the two primes below 5.

These programs are deterministic integer tallies, so a correct re-run on
different hardware with a different compiler is byte-identical. Anything less
would have been a finding.

Together with the earlier `crossbase_qr` @ 10⁹ audit and `crossbase` @ 2·10⁸,
**all four Paper 3 C programs have now been independently reproduced.**

## Note: a real discrepancy, but not a computational one

`crossbase_om.c` in the public repo has sha256 `5661c0b4…` while the local
copy has `edacf378…`. The difference is **comment-only**: the repo version
still carries the copy-pasted header

```
 * gcc -O3 -o crossbase crossbase.c -lm
 * ./crossbase <limit> <out.json>
```

which builds the wrong binary if followed literally. That was fixed locally
earlier today. Stripping the two header lines from both copies gives the
identical hash `eac0cf7022412d3c736bc3e330084592bb0c841d96e0d2f3eab490c47d183650`
— so the compiled behaviour is the same, and the byte-identical output above
is not affected.

**Action required:** push the header fix to the public repo, or a referee
following the shipped instructions will build `crossbase` from
`crossbase_om.c`'s instructions and be confused.
