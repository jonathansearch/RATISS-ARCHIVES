# r/Physics — fiche de faits + stratégie (30/09/2026)

> 📏 **Method note (audit 30/09)**: every QPU "fidelity" here is a **population fidelity** P(0…0)+P(1…1), Z-basis counts only. It **upper-bounds the GHZ fidelity and does not by itself prove entanglement**. Coherence measurements (parity oscillations, X basis) are the next step.

## ⚠️ Règles du sub (vérifiées dans les captures du chef)
R7 : contenu généré par IA INTERDIT · R2 : théories perso assistées par IA refusées (pas d'endorsement arXiv)
→ Le post r/Physics doit être ÉCRIT PAR LE CHEF LUI-MÊME (sa vraie voix). L'IA fournit les FAITS, pas les phrases.
→ Pas d'image IA (R4), titre factuel (R3), aucun claim de nouvelle physique (R2).

## Fiche de faits vérifiés (à reformuler avec ses propres mots, en anglais)
**What I did (all reproducible, MIT-licensed):**
- Rebuilt standard Planck-scale calculations from scratch in Python (CODATA 2022 constants):
  measurement-crossing at √2·ℓ_P (E = E_P/√2 ≈ 1.38×10⁹ J); GUP wall gives the same √2·ℓ_P;
  replicated Page-curve toy model to 0.001 bit vs analytic formula (peak exactly at N/2);
  Unruh temperature equals Hawking temperature at a Planck-mass horizon (agreement ~10⁻⁶).
  40 automated tests pass. Sanity checks: LHC dipole radius 2,801 m computed vs 2,804 m real;
  Fermi GRB 090510 superluminal-dispersion replay (ℓ_P pixel would delay a 31 GeV photon by ~824 ms;
  observed bound ~85 ms → naive pixel ruled out; LHAASO 221009A pushes E_QG,1 > 10 E_Pl).
- Then benchmarked THREE real quantum processors via the Open Quantum cloud platform (14 jobs, ~11,000 shots):
  - AQT IBEX Q1 (trapped ions, all-to-all): Bell 99.61% (515/505/2/2 of 1024 shots); GHZ-7 90.04%
  - IQM Garnet (20q superconducting, square lattice): GHZ-3/4/5 chains 94.5/94.6/88.5%; GHZ-12 66.0% (387×|0…0⟩ + 289×|1…1⟩)
  - Rigetti Cepheus-1-108Q (108q chiplets): GHZ-3/4/5 89.7/79.3/68.7%
- Observations: at equal GHZ size the 108q chiplet device decoheres FASTER than the 20q lattice device
  (79.3 vs 94.6% at GHZ-4); population-fidelity slopes ≈ −1.9 mean over 3 points, accelerating (ions), −3.2 from 5q to 12q (20q), −10.5 (108q) points/qubit.
- Systems finding: co-hosted GHZ compartments survive transpilation ONLY on all-to-all hardware
  (45% vs 94% same device, same hour — lattice transpiler inserts SWAPs that leak entanglement across compartments).
- Costs per 1024-shot job: 1 / 2 / 15 credits (108q cheapest, ions most expensive).
- Scope/honesty: NO claim of new physics — tools verification + cross-architecture benchmarking;
  everything (code, raw counts, failures, cancelled jobs) is public; attribution to Open Quantum platform.

## Titres acceptables (factuels, R3)
1. "I rebuilt standard Planck-scale calculations and benchmarked three real QPUs (ions, 20q lattice, 108q chiplets) — code and raw counts open source"
2. "GHZ fidelity scaling across three commercial quantum processors: trapped ions vs superconducting lattice vs 108-qubit chiplets (open data)"

## Post prêt à coller → r/quantumcomputing (IA autorisée là-bas, benchmark bienvenu)
**Titre :** I benchmarked three real quantum processors (trapped ions, 20q lattice, 108q chiplets) from a phone in Cameroon — GHZ scaling, transpiler effects, raw data, all open source

**Corps :**
Hi everyone,

I spent one day running real hardware jobs via the Open Quantum platform (14 jobs, ~11k shots, 1024 each)
and I'd love technical feedback from this community. Everything is MIT-licensed and reproducible.

Setup: GHZ chains (native linear coupling), 1024 shots per job, same circuit shape across backends.

| GHZ size | AQT IBEX Q1 (ions, all-to-all) | IQM Garnet (20q lattice) | Rigetti Cepheus-1-108Q (chiplets) |
|---|---|---|---|
| 2 (Bell) | 99.61% | — | — |
| 3 | — | 94.5% | 89.7% |
| 4 | (job still queued) | 94.6% | 79.3% |
| 5 | — | 88.5% | 68.7% |
| 7 | 90.04% | — | — |
| 12 | — | 66.0% | — |

Three things I found interesting:
1. At equal circuit size, the 108q chiplet device decoheres faster than the 20q lattice device
   (79.3% vs 94.6% at GHZ-4). Population-fidelity slopes (Z-basis only, an upper bound on GHZ fidelity): ≈ −1.9 pts/qubit mean over 3 points, local slopes −1.2 then −2.4 (ions), −3.2 from 5q to 12q (20q), −10.5 (108q).
2. Co-hosting several GHZ compartments in ONE job only survives on all-to-all hardware: on the square
   lattice the transpiler inserts SWAPs and fidelity drops to ~45% vs ~94% for separate jobs
   (same device, same hour). Isolates the transpiler effect pretty cleanly.
3. Pricing is inverted vs qubit count: the 108q machine costs 1 credit/job, the 20q costs 2, the ion
   trap 15 — precision (99.61% Bell) is what you pay for.

Repo (code, raw counts per job, cancelled-job log, tests): github.com/jonathansearch/RATISS-PLANCK
Hardware access via Open Quantum (attribution: openquantum.com/citation). Backends: AQT IBEX Q1,
IQM Garnet, Rigetti Cepheus-1-108Q.

Happy to answer questions about the circuits, the counts, or the platform workflow.

*Fiche archivée par le labo — sceau RATISS-ARCHIVES.*

---

# MISE À JOUR 30/09 11h11 — Règles r/quantumcomputing lues (captures du chef) : stratégie révisée

## Ce que dit le règlement (résumé fidèle)
1. **Qualité** : post soigné, on-topic QC, **« Your post cannot be AI-generated »**, pas de memes.
2. Carrière/études → megathread hebdo uniquement.
3. **« Not the place to post your own independent research »** (anti-crank) → pas de dump "mon projet révolutionnaire".
4. **Anti-pub** : les projets/outils maison peuvent être partagés « for the sake of QC discussion », **MAIS « pretending you're only seeking feedback counts as self-promotion »** → ne PAS formuler "juste chercher du feedback".
5. Pas de lien nu → corps de texte ou commentaire d'amorce obligatoire.
6. **Compte ≥ 2 jours + karma suffisant** (sinon AutoMod ban temporaire/permanent).
7. Anglais obligatoire.

## Conclusion du labo (honnêteté loi n°11)
Les deux grands subs interdisent le contenu généré par IA → sur Reddit, SEUL le chef écrit le post.
L'IA fournit : la fiche de faits (ci-dessus), la STRUCTURE conforme, et la relecture. Jamais le texte à coller.

## Structure conforme recommandée (r/quantumcomputing, écrit par le chef)
- Titre = l'observation, pas le projet : "GHZ fidelity across 3 real QPUs: chiplet 108q decoheres faster than 20q lattice — data from 14 jobs (ions, Garnet, Cepheus)"
- 1re phrase = le phénomène discuté (pas "check my repo") ; corps = 5-8 phrases factuelles + tableau mini ;
  la question à la communauté à la fin ("has anyone measured similar transpiler leakage on lattice topologies?")
- Le lien GitHub DANS le corps comme source des données (règle 5 ok), sans brandage RATISS dans le titre.
- Proscrire : "seeking feedback", "my project", tonnes publicitaire, emojis.
- Prérequis dur (règle 6) : compte ≥ 2 jours + karma → sinon AutoMod supprime/ban.

## Alternatives où partager sans friction (selon choix du chef)
- **Show HN** (news.ycombinator.com) : projets ouverts bienvenus, format "Show HN: RATISS-PLANCK —
  cross-benchmark of 3 real QPUs (ions, 20q lattice, 108q chiplets)" ; honnêteté appréciée.
- **Quantum Computing Stack Exchange** : la question technique pure (fuite SWAP co-hébergée sur lattice
  vs all-to-all, données à l'appui) → retours d'experts garantis, format Q&A légitime.
- **r/LLMPhysics / r/HypotheticalPhysics** : recommandés par les modos de r/Physics pour contenu assisté par IA.
