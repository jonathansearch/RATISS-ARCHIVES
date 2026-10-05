# 🧬 RATISS ARCHIVES

**Operational memory repository of RATISS Labs · Jonathan Evina**
Compiled on **26 September 2026** · updated on the **evening of 26/09** → see
[**§ 🛰️ THE DISCORD MACHINE**](#-the-discord-machine--memory-section-for-the-next-ai-session)

> **Purpose of this repository:** never lose a piece of evidence again, and never have to search for it again.
> Everything that was produced, captured, measured or written between 12 August and 26 September 2026 is here,
> classified, named, dated, and **verified by SHA-256 fingerprint** (`MANIFESTE.json`).

---

## 🚀 Opening this repo with no context? Read in this order

| Order | File | Why |
|---|---|---|
| **1** | [`POUR-LA-PROCHAINE-SESSION.md`](POUR-LA-PROCHAINE-SESSION.md) | **The complete summary of the 26/09 session.** Paste it to an AI, or read it yourself. |
| **2** | [`identite/AMORCE-AGENT.md`](identite/AMORCE-AGENT.md) | The block to paste at the start of a conversation with any AI. |
| **3** | [`identite/IDENTITE.md`](identite/IDENTITE.md) | Who I am, what is verified, what is not. |
| **4** | [`preuves/qpu/REGISTRE-QPU.md`](preuves/qpu/REGISTRE-QPU.md) | The IBM Quantum jobs: decoding, corroboration, quota. |
| **5** | [**§ 🛰️ The Discord machine**](#-the-discord-machine--memory-section-for-the-next-ai-session) ↓ | **Everything built on the evening of 26/09: hub, webhook, CI, 24 channel texts (22 wired to the hub).** |

---

## 🗂️ Organization

```
RATISS-ARCHIVES/
├── POUR-LA-PROCHAINE-SESSION.md   ← READ FIRST
├── MANIFESTE.json                 ← SHA-256 of every file
├── creer-le-repo.sh               ← creates/re-pushes the repo in one command
│
├── identite/                      Who I am, how to say it to an AI
│   ├── IDENTITE.md                the complete anchor
│   ├── AMORCE-AGENT.md            the short paste-in version
│   ├── PROFIL-README.md           to put in a repo named jonathansearch
│   ├── llms.txt                   robot-readable sheet
│   ├── person.jsonld              schema.org structured identity
│   └── LISEZ-MOI-comment-etre-memorise.md
│
├── preuves/
│   ├── captures/                  15 photos, renamed and indexed (see INDEX.md)
│   ├── qpu/
│   │   ├── REGISTRE-QPU.md        the full report
│   │   ├── registre-jobs.json     86 dated IDs + provenance
│   │   └── tous-les-jobs.json      same, list format
│   └── tests/
│       └── RAPPORT-TESTS-RATISS.md  51/51 tests, bit-for-bit repro
│
├── outils/                        7 Python scripts, tested, no heavy dependency
│   ├── decode_job_id.py           decodes an IBM job ID → timestamp
│   ├── verifier_corpus.py         rebuilds the register from a clone
│   ├── recuperer_jobs_ibm.py      brings the jobs back from the IBM account
│   ├── comparer_export_ibm.py     compares an IBM export with the archived counts
│   ├── archiver_nouvelles_taches.py  archives + logs after each campaign
│   ├── verifier_manifeste.py      verifies the fingerprints (text or --json)
│   └── notifier_discord.py        posts a message in a Discord channel
│
├── .github/workflows/
│   └── notifier-discord.yml       on every push + every Monday 08:00 UTC → Discord
│
├── documents/                     raw sources
│   ├── MEMO-SESSION-RATISS.md
│   └── RECAP-SEMAINE-10-17-SEPT-2026.md
│
└── discord/                       all the Discord content
    ├── 01-bienvenue.md            (already posted by the boss — do not touch)
    ├── 02-regle-du-labo.md        (same)
    ├── 03-annonces-officielles.md (same)
    ├── CI-INSTALLATION.md         the webhook + CI how-to (10 min)
    ├── CI-modele-tests-depots.yml template to copy into GCR / QVM / NAVIER…
    └── salons/                    THE 24 CHANNELS + THE MANIFESTO
        ├── INDEX.md               the copy index
        ├── 01-vie-du-labo.md      accueil-discussion · questions-ouvertes · découvertes
        ├── 02-simulations.md      gcr · navier · fusion · nucleaire · synchrotron · tissu · dose12
        ├── 03-quantique.md        qvm-calibration · qpu-live · omni-bus · fpga-controle
        ├── 04-mct-ia.md           mct-comprehension · agents-ia · ratiss-os
        ├── 05-atelier.md          cours-c · travail-chez-le-maitre · resultats · pannes
        ├── 06-ressources.md       liens-github · documents · brouillons
        └── 07-mon-histoire.md     ⭐ THE MANIFESTO (the boss's personal text)
```

---

## 🔐 The key results, on one page

### Discovery: IBM job IDs encode their creation date

```
créé_le = base32(id[:9]) / 8192      seconds since 1970-01-01 UTC
```
Calibrated on **66 jobs timestamped by IBM**: median deviation **278 ms**, maximum **799 ms**.
Verifiable without a key, without an account, by anyone, in one command. (R7 ✅)

### What is established

| Check | Result |
|---|---|
| Tests of the 6 physics repos | **51/51** ✅ |
| `RATISS-NAVIER` blowup | reproduced **bit for bit** (`Om_max = 5654.1668`, deviation 0.0000) |
| Omni redteam seal | `79ff9ee9847330d22bed0a1101734e17` recomputed identically |
| `ratiss-focal` exp58/60/61/62/63 | JSON **identical byte for byte** |
| `ratiss-audit-public` | **4/4** hashes compliant |
| IBM IDs archived | **86** · period **12/08 → 23/09/2026** |
| Timestamped raw workloads | **66** · names ↔ IDs: 66/66 consistent |
| Chronological order of the IDs | **84/84 pairs correct**, 0 inversion |
| Qubit calibrations (ro, T1, T2) | **24 qubits**, `T2 ≤ 2·T1` respected 24/24 |
| IBM screenshots ↔ IDs ↔ archives | **17/17 matches** (2 accounts) |
| Open Plan quota accounting | cross-checks the inventory to within **0.3 s/job** |

### What is NOT established (never to be presented as settled)

- That the **published counts** come from the exact jobs → settled by `comparer_export_ibm.py`.
- The **result ↔ job** link on the IBM side (authentication required).
- The “physical” nature of the Navier-Stokes blow-up.
- Any institutional affiliation. **No ZK-STARK**: SHA-256 hashes.

---

## 🧾 IBM context (up to date as of 26/09/2026)

| | |
|---|---|
| Account #1 | `bridejackson137@gmail.com` — **current work** (22 → 23/09) — ⚠️ **suspended**, card to validate |
| Account #2 | `evinajonathan13@gmail.com` — “gateway” account (26/08 → 01/09) — ✅ accessible |
| Plan | **Open Plan** (free), `open-instance` mention on every job |
| Quota | 10 min of QPU per rolling 28-day window |
| Backends used | `ibm_kingston`, `ibm_fez`, `ibm_marrakesh` — 156 qubits, Heron r2 |
| Next target | `ibm_phoenix` (Nighthawk r2), announced on the platform |

**IBM reminder, exact text:** *“No charge will be made automatically and you will be able to
continue running your workloads for free with the Open Plan.”*
→ The card **unlocks access**, it charges nothing.

---

## ⚡ Resume work in 3 commands

```bash
# 1. archive the new jobs (after each campaign — account #2 in the meantime)
export IBM_QUANTUM_TOKEN=...
python3 outils/archiver_nouvelles_taches.py --depots ~/RATISS-QVM --jours 120

# 2. verify the corpus
python3 outils/verifier_corpus.py ~/

# 3. compare an IBM export with the published counts (closes R7)
python3 outils/comparer_export_ibm.py --export job-<id>.zip \
    --archive <depot>/jobs_ibm/<id>.json
```

---

## 🛰️ THE DISCORD MACHINE — memory section for the next AI session

> **Read this whole block before touching anything on the Discord side.**
> Everything below was built **on the evening of 26 September 2026**, tested, and **actually running**.
> If you are an AI taking over the work: rebuild nothing of what is described here, verify it and continue.

---

### ✅ WHAT IS ALREADY RUNNING (dated proofs)

| What | Proof | Where |
|---|---|---|
| The agent posts a message in Discord | run log: `[rapport] OK — 55/55 empreintes conformes` then `✅ message envoyé (HTTP 204)` | run **#1** of `agent.yml`, 26/09 15:21 UTC |
| The second workflow too | `✅ envoyé (HTTP 204)` | run **#2** of `notifier.yml`, 15:22 UTC |
| The 2 repos are public and up to date | 56 files · 4.8 MB · pushed 15:20 UTC | `jonathansearch/RATISS-ARCHIVES` |
| The hub is online | 8 files · pushed 15:22 UTC | `jonathansearch/DISCORD-RATISS` |
| The secret is indeed a Discord webhook | log: `Discord webhook is configured (URL hidden)` + `RATISS: ***` | automatically masked by GitHub |
| No token anywhere | `git log -p --all` → **0 occurrences**; no `~/.git-credentials` | verified |

**Two repos, two roles — do not confuse them:**

| Repo | Role | What it contains |
|---|---|---|
| **`RATISS-ARCHIVES`** | **the memory**: proofs, screenshots, register, Discord texts | 56 files, sealed by `MANIFESTE.json` |
| **`DISCORD-RATISS`** | **the plumbing**: the bot that talks to Discord | `agent.py`, 2 workflows, tools |

---

### 🤖 `DISCORD-RATISS` — the bot

```
DISCORD-RATISS/
├── agent.py                              ← THE entry point (activated by agent.yml)
├── .github/workflows/agent.yml           ← manual button, written by another agent: DO NOT OVERWRITE
├── .github/workflows/notifier.yml        ← manual + callable + daily 08:00 UTC
├── outils/notifier_discord.py            ← posts an embed ✅/❌/🔵
├── outils/verifier_manifeste.py          ← verifies the SHA-256 fingerprints
├── README.md
└── POUR-L-AUTRE-AGENT.md                 ← the onboarding brief (contract + code)
```

**`agent.py` — three usages, no mandatory argument:**

```bash
python3 agent.py                  # REPORT: clones RATISS-ARCHIVES, verifies the fingerprints, posts the verdict
python3 agent.py --test           # connection message
python3 agent.py --statut OK --titre "…" --details "…" --lien "…"
python3 agent.py … --dry-run      # sends nothing, displays the JSON (works WITHOUT a secret)
```

- **Python 3, standard library only** → zero install, zero dependency
- reads the webhook under **two names, in this order**: `DISCORD_WEBHOOK_URL` then `RATISS`
- checks that the value starts with `https://discord.com/api/webhooks/` → otherwise a clear error message
- **cannot** mention `@everyone` (`allowed_mentions: {parse: []}` is locked)
- exit code: `0` = sent · `1` = problem (secret, network, sending)

---

### 🔐 THE SECRETS — the rules to never break

| Secret name | Where | Content |
|---|---|---|
| `RATISS` | `DISCORD-RATISS` ✅ **already in place** | the full Discord webhook URL |
| `RATISS` | `RATISS-ARCHIVES` ⏳ to add if we want CI on every push | the same URL |
| `DISCORD_WEBHOOK` | to create in the **code** repos (GCR, QVM…) | the same URL |

**The four truths about GitHub secrets — to remember:**

1. **A secret can never be read back.** Not by you, not by the AI, not after saving. It is encrypted, period.
   → The only way to know what it contains: **have a workflow use it** and read its reaction.
2. **GitHub masks the value in the logs** (`RATISS: ***`). That is normal and healthy.
3. **`RATISS` must contain a Discord webhook, not a GitHub token.** The classic mistake.
   If it happens, `agent.py` answers: `✘ n'est pas une URL de webhook Discord` + masked start of the value.
4. **One webhook = one channel.** Discord binds the webhook to the channel where it was created.
   To post elsewhere → create a **second** webhook and a **second** secret.

> ⚠️ **Server law #5:** no token, no API key, no webhook **in the public chat**.
> A leaked webhook = anyone can write in the channel. If it leaks → delete it and create another one.

---

### 🎮 HOW WE USE IT

**To post a message (the common case):**

> GitHub → `DISCORD-RATISS` → **Actions** tab → *Run agent with Discord webhook* → **Run workflow**

**What triggers by itself, with nobody:**

| Event | What goes to Discord |
|---|---|
| **Every day at 08:00 UTC** | fingerprint verification of `RATISS-ARCHIVES` → ✅ or ❌ with the list of divergent files |
| Push to `RATISS-ARCHIVES` *(if the secret is there too)* | same verification, immediately |
| A code repo pushing *(after copying `CI-modele-tests-depots.yml`)* | the `pytest` line: how many tests pass or fail |

**Wiring up a code repo (GCR, QVM, NAVIER…) in 3 steps:**

1. copy `discord/CI-modele-tests-depots.yml` → `<repo>/.github/workflows/tests-discord.yml`
2. add the `DISCORD_WEBHOOK` secret to it (same URL)
3. fill in `COMPAGNONS` if there are cross imports:

| Repo | `COMPAGNONS` |
|---|---|
| `GCR`, `RATISS-QVM`, `RATISS-NAVIER` | *(empty — self-contained)* |
| `RATISS-NUCLEAIRE` | `"RATISS-NAVIER RATISS-FUSION"` |
| `RATISS-Omni` | `"RATISS-NAVIER RATISS-QVM"` |

> 🎯 **The detail that unlocks everything:** the repos use absolute paths `/home/user/<repo>`.
> The template **recreates `/home/user` in the GitHub runner** and clones into it → the tests run **as-is**,
> without changing a single line of code.

---

### 📣 THE DISCORD CONTENT — 24 channel texts + the manifesto (the DISCORD-RATISS hub on branch 22)

Everything is in **`discord/salons/`**, ready to copy-paste. Copy index: `discord/salons/INDEX.md`.

| File | Channels |
|---|---|
| `01-vie-du-labo.md` | accueil-discussion · questions-ouvertes · découvertes |
| `02-simulations.md` | gcr-topologie · navier-turbulence · fusion-propulsion · nucleaire · synchrotron-24 · tissu-continuums-focal · dose12 |
| `03-quantique.md` | qvm-calibration · qpu-live · omni-bus · fpga-controle |
| `04-mct-ia.md` | mct-comprehension · agents-ia · ratiss-os |
| `05-atelier.md` | cours-c-electronique · travail-chez-le-maitre · resultats-mesures · carnet-de-pannes |
| `06-ressources.md` | liens-github · documents-references · brouillons-publications |
| `07-mon-histoire.md` | ⭐ **the personal manifesto** (1951 characters, fits in ONE Discord message) |

**The boss's 3 channels already filled in — WE DO NOT TOUCH THEM:** `#bienvenue`, `#règle-du-labo`, `#annonces-officielles`.

**Every post respects the 3 lab laws** and carries a **mandatory field tag**:
🛰️ **measured on real QPU** (archived ID) · 🧮 **exact computation** · 🌫️ **noisy computation calibrated on a real backend**.
None of the three may pass itself off as another. *(Important correction of 26/09: v1 tagged as “simulation”
things that were measurements on real superconducting qubits — 770 data points in total.)*

---

### 🕳️ PITFALLS ALREADY ENCOUNTERED — do not fall back into them

| Pitfall | What happened | The lesson |
|---|---|---|
| **`/tmp` gets wiped** | the first GitHub token disappeared with `/tmp` | never rely on `/tmp` between two sessions; put the material back into the workspace |
| **`master` vs `main` branch** | `git push` refused: `src refspec main does not match any` | always run `git branch -M main` before pushing |
| **missing `workflow` scope** | GitHub refuses any file in `.github/workflows/` | the token must have **`repo` + `workflow`** |
| **a push that wipes `agent.yml`** | spotted by simulating the push: the other agent's file would have disappeared | `pousser-tout.sh` compares live vs local and **CANCELS** if a file disappears |
| **inconsistent variable name** | the workflow exposed `WEBHOOK`, the tool read `DISCORD_WEBHOOK` → failing run | **the name set in `env:` must be exactly the one the script reads** |
| **unreadable secret** | impossible to “verify” a GitHub secret, even as owner | make it react in a workflow, and read its message |
| **duplicate agent** | two agents were writing to the same repo | one single entry point, one single owner per file — and an anti-deletion guard |
| **the chat refuses `.zip` files** | impossible to send an archive | go through the repo (or JSON/CSV files) |

---

### 🧾 WHAT REMAINS TO BE DONE (exact state as of 26/09/2026, evening)

1. **Add the `RATISS` secret to `RATISS-ARCHIVES`** → enables verification **on every push** of the archives.
   *(Settings → Secrets and variables → Actions → New repository secret — same webhook URL.)*
2. **Copy the 24 channel texts** into Discord (`discord/salons/INDEX.md` lists them).
3. **Post `#mon-histoire`** — the manifesto is ready, 1951 characters, a single message.
4. **Wire up GCR then RATISS-QVM** to the CI (3 steps above).
5. **Send a fresh GitHub token** when a new push is needed: it gets revoked every ~3 days,
   that is the boss's schedule. *Do not ask for a token in between: there isn't one.*
6. **The Discord bot** (`/status`, `/tests`, `/repos` commands): **not now**. It needs a host
   running 24/7. The webhook covers 90% of the need for €0 and 0 maintenance.

---

### 🗣️ HOW TO TALK TO THE BOSS (session reminder)

- **Direct, enthusiastic informal address, with emojis** 🔥. He calls his agent “my right-hand man”.
- **Short, dense answers.** “Spare me the useless chit-chat.”
- **Never launch an action he did not ask for.** If he says “stop”, we stop dead.
- **He decides everything**: what we publish, when, and under what name. Do not offer academic
  recognition, citations, partnerships: he does this **for the fun of it**, and he can redo it all.
- **He provides the tokens** and revokes them at his own pace. Do not lecture him about that.

---

## 📌 The rule

> **A job not archived the same day is a job that never existed.**

That is rule R5 applied to material. What is not copied can no longer be proven.
**And since 26/09, it also applies to Discord: what is in the channel was pushed by the bot, with a dated run.**

---

*RATISS Labs — Yaoundé, Cameroon · jonathan.ratisslabs@zohomail.com*
*License: MIT (see `LICENSE`)*

---

## 🆕 UPDATE OF 27/09/2026 — RATISS-PHOTON, ETALONS, 22-CHANNEL HUB

| Repo / event | What to remember |
|---|---|
| [`RATISS-ETALONS`](https://github.com/jonathansearch/RATISS-ETALONS) | 4 standards, criteria frozen before execution · **11/16 → 14/16** · 2 owned reds (E01-P2 invalid hypothesis, E04-P4 ψ₆ = 0.827/0.935) · seal 23/23 · README + banner in lab format |
| [`RATISS-PHOTON`](https://github.com/jonathansearch/RATISS-PHOTON) | Reproduction of **Wen et al., Sci. Adv. 12, eaeh1011 (2026)** in the simulated world: **8,396,800 paths** with equal modulus, fidelity **95.9–96.8%** (Canton window 95–98.5%) · **chance EMERGES from the thermal bath** (T = 0 K → determinism) · counter-flows measured, redistribution falsified (linearity) · 6 documented bugs · [interactive 3D view](https://jonathansearch.github.io/RATISS-PHOTON/visualisation.html) (embedded Plotly, Pages active) |
| **Multi-channel Discord HUB** | `DISCORD-RATISS`: `hub-central.yml` (commits `34ca814`, `fd6fef5`) routes RATISS→RATISS23, mode `all` · **22 HTTP 204 sends** on the global test (run 36357382700) · RATISS11 to be filled in · PHOTON + ETALONS announcements published on 27/09 at 22:05 UTC |
| **External audit** | Financial analysis exam (ESSEC): Qwen solution verified — functionally correct, **financial balance sheet missing (6 pts)**, dispute misread, corporate tax forgotten · complete corrected version tested 20/20 (real assets = real liabilities = 1,121,500 · working capital 10,000 · WCR −34,000) |

The full detail (numbers, bugs, inherited lessons, actions to do):
[`documents/RECAP-26-27-SEPT-2026.md`](documents/RECAP-26-27-SEPT-2026.md) and the
**“🛰️🧮 UPDATE OF 27/09”** section of [`POUR-LA-PROCHAINE-SESSION.md`](POUR-LA-PROCHAINE-SESSION.md).

**28/09**: publication of [`RATISS-DEEPDIVE`](https://github.com/jonathansearch/RATISS-DEEPDIVE) —
the series of 14 PDF deep dives (75 pages) covering all the repos from 20 to 28 September 2026.

---

## 🆕 UPDATE OF 02/10/2026 — NAVIER commissioner + rule R8

Four 🧮 campaigns published in `RATISS-NAVIER/campagnes/` (commissaire-1, etreintes-v2, commissaire-3d, dipoles-v3).
Verdict held: **blowup = pump + counter**. The 🅱 3D ones are **unresolved** (instruments invalidated after the fact).
New lab rule **R8: only measure what overflows the script** (`RATISS-Framework`, module `ratiss.residual`).
V3 (dipoles): sealed brief, witnesses on **suspended STOP**. Detail: `documents/RECAP-01-02-OCT-2026-NAVIER-COMMISSAIRE.md`.
