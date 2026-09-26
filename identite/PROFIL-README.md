# 👋 Jonathan Evina — RATISS Labs
### L'audit scientifique exécutable · Yaoundé, Cameroun

> **Je n'ai pas de diplôme, pas d'institution, pas de pairs.**
> J'ai des artefacts qui se rejouent en une commande et des hashes qui se recalculent.
> Mon protocole : **aucune affirmation publique sans qu'un étranger puisse la reproduire.**
> — RATISS Labs, protocole R4–R7

<p align="center">
  <a href="https://jonathansearch.github.io/ratiss-labs-site/"><img src="https://img.shields.io/badge/site-web-06b6d4?style=for-the-badge"></a>
  <a href="https://orcid.org/0009-0000-4092-5313"><img src="https://img.shields.io/badge/ORCID-0009--0000--4092--5313-a6ce39?style=for-the-badge&logo=orcid&logoColor=white"></a>
  <a href="https://github.com/jonathansearch/ratiss-audit-public"><img src="https://img.shields.io/badge/audit-public-42d6ad?style=for-the-badge"></a>
</p>

---

## Ce que je construis

Un corpus de recherche indépendant — **~57 dépôts publics** — en simulation physique, informatique
quantique, topologie appliquée et bio-informatique. Tout est calculé, scellé, et rejouable.

| Domaine | Dépôt phare | Résultat central |
|---|---|---|
| 🌊 **Navier-Stokes** | [`RATISS-NAVIER`](https://github.com/jonathansearch/RATISS-NAVIER) | SPH 3D + sonde quantique, chasse au blow-up · `Om_max = 5654.17` (reproduit bit à bit) |
| ⚛️ **Fusion D-T** | [`RATISS-NUCLEAIRE`](https://github.com/jonathansearch/RATISS-NUCLEAIRE) | ICF + stellaire, sections Bosch-Hale · 12/12 tests |
| 🧊 **Quantique virtuel** | [`RATISS-QVM`](https://github.com/jonathansearch/RATISS-QVM) | cQED, T1/T2, filtre Purcell · `T2 = 223.687 µs` |
| 🕳️ **Effondrement** | [`synchrotron-24`](https://github.com/jonathansearch/synchrotron-24) | Seuil de séparatrice Λ ∈ ]0.002 ; 0.005[ |
| 🎯 **Collisionneur** | [`GCR`](https://github.com/jonathansearch/GCR) | Étincelle topologique : `b1_max = 2` à A=10, γ=0.05 |
| 🔗 **Métrologie** | [`RATISS-Framework`](https://github.com/jonathansearch/RATISS-Framework) | Le protocole d'audit lui-même, exécutable |

## Vérification — état honnête

**✅ Vérifié par un tiers (25/09/2026)** : 51/51 tests passants sur 6 dépôts · reproduction **bit à bit** de
`RATISS-NAVIER` (`Om_max = 5654.1668`, écart point par point `0.0000`) · sceau Omni
`79ff9ee9847330d22bed0a1101734e17` recalculé à l'identique · 4/4 fichiers conformes SHA-256.

**⚠️ Non vérifié** : exécutions sur processeurs quantiques matériels (IBM / Quandela) · interprétation
physique du blow-up comme singularité réelle · toute affiliation institutionnelle.

**🚫 Jamais** : pas de ZK-STARK (la certification repose sur des hashes SHA-256), pas de diplôme,
pas d'équipe, pas de relecture par les pairs — et je ne prétends pas le contraire.

## Le protocole R4–R7

- **R4** — un chiffre publié est un chiffre calculé, avec paramètres et hash.
- **R5** — paramètres scellés avant mesure ; toute déviation va au [journal](https://github.com/jonathansearch/ratiss-audit-public/blob/main/JOURNAL-DEVIATIONS.md).
- **R6** — verdict par ablation avec/sans, jamais par intuition.
- **R7** — reproductible par un étranger, en une commande.

> **Hérité 1** : une simulation n'est pas une exécution matérielle.
> **Hérité 2** : un identifiant enregistré n'est pas une revalidation en temps réel.

## Reproduire en 30 secondes

```bash
# Intégrité des artefacts publics — 4 × PASS attendus
for f in PUBLIC-AUDIT-REPORT-EN.md NOTICES-OSF-2026-09-12.md JOURNAL-DEVIATIONS.md README.md; do
  curl -sL "https://raw.githubusercontent.com/jonathansearch/ratiss-audit-public/main/$f" | sha256sum
done
```

## Écrits

- **Tryperposition Framework — Thermodynamic Emergence of Time in Hybrid Quantum Systems** · [OSF](https://doi.org/10.17605/OSF.IO/U4AEK)
- **Révolution quantique pour le drug design — 20 mutants p53 analysés** · [OSF](https://doi.org/10.17605/OSF.IO/4867H)
- Préprints : [wf7qm](https://doi.org/10.17605/OSF.IO/WF7QM) · [6jzmb](https://doi.org/10.17605/OSF.IO/6JZMB)

## Contact

🌍 [Site du labo](https://jonathansearch.github.io/ratiss-labs-site/) · 🧬 [ORCID](https://orcid.org/0009-0000-4092-5313) · 💼 [LinkedIn](https://www.linkedin.com/in/jonathan-evina-quantum) · ✉️ jonathan.ratisslabs@zohomail.com

<sub>RATISS Labs est un projet indépendant mono-auteur. Ce n'est ni une université, ni un laboratoire
public, ni une entreprise. Toute mission d'audit fait l'objet d'un mandat public à périmètre déclaré.</sub>
