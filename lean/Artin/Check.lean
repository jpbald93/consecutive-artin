import Artin.Exclusion
import Artin.Bridge
import Artin.TripleExclusion
set_option linter.style.header false
/-! Axiom audit + the fully bridged exclusion theorem. -/
namespace ArtinExclusion
open ZMod

/-- **Theorem 1 of the paper, in terms of the real Legendre symbol.**
If `p` and `p'` are primes other than 2 and 5 whose residues mod 40 differ by
20, then `(10|p') = -(10|p)`; consequently they cannot both satisfy
`(10|·) = -1`, so at most one is an Artin prime for base 10. -/
theorem legendreSym_flip_of_shift_twenty
    {p p' : ℕ} [Fact p.Prime] [Fact p'.Prime]
    (hp2 : p ≠ 2) (hp5 : p ≠ 5) (hq2 : p' ≠ 2) (hq5 : p' ≠ 5)
    (hshift : (p' : ZMod 40) = (p : ZMod 40) + 20)
    (hunit : IsUnit ((p : ZMod 40))) :
    legendreSym p' 10 = - legendreSym p 10 := by
  rw [← chi10_eq_legendreSym hq2 hq5, ← chi10_eq_legendreSym hp2 hp5, hshift]
  exact chi10_shift_twenty _ hunit

/-- At most one of the two primes is an Artin prime for base 10. -/
theorem not_both_artin
    {p p' : ℕ} [Fact p.Prime] [Fact p'.Prime]
    (hp2 : p ≠ 2) (hp5 : p ≠ 5) (hq2 : p' ≠ 2) (hq5 : p' ≠ 5)
    (hshift : (p' : ZMod 40) = (p : ZMod 40) + 20)
    (hunit : IsUnit ((p : ZMod 40))) :
    ¬ (legendreSym p 10 = -1 ∧ legendreSym p' 10 = -1) := by
  intro h
  have := legendreSym_flip_of_shift_twenty hp2 hp5 hq2 hq5 hshift hunit
  rw [h.1, h.2] at this
  norm_num at this

end ArtinExclusion

open ArtinExclusion
#print axioms chi10_shift_twenty
#print axioms chi10_shift_zero
#print axioms not_both_nonresidue
#print axioms chi10_eq_legendreSym
#print axioms legendreSym_flip_of_shift_twenty
#print axioms not_both_artin
#print axioms not_all_three_nonresidue
#print axioms legendreSym_third_eq_one
#print axioms not_all_three_nonresidue_two_five_ten
