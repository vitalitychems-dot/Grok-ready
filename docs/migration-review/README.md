# Source omission review — not a migration sign-off

Shared review: https://github.com/vitalitychems-dot/Grok-ready/issues/1

Compared candidate: `4072851ad13536b3e65cbd7fecfe73d306038d32` (1,578 files). The candidate is not yet accepted as the final migration. This review adds archival evidence and missing source files without overwriting its application.

## Findings

- **443 files absent at their original paths are already represented by identical Git blob hashes at other paths.** See `represented-at-other-paths.json`; these must not be restored as redundant copies.
- **119 byte-unique source-code files were not found anywhere in that candidate:** 113 TSX files and six Python/MJS helpers. They are preserved under `archives/migration-review/`, with original paths and hashes in `preserved-source-files.json`. They are not wired into the active application; agents must determine which features to integrate or explicitly document as superseded.
- The local LFS ZIP has a verified SHA-256 and ZIP CRC. The salvage index selects 154 source paths (106 TSX, 40 PNG, eight TXT); 152 names occur at the recorded paths, and the other two TSX blobs are present under alternate archive paths with matching Git blob hashes. PR #2 includes the 106 TSX payloads among its 119 archived source files. The 40 PNG and eight TXT payloads remain untransferred and require visual/privacy review. See `local-archive-salvage.json`; the original ZIP itself is not copied to Grok-ready.
- The three remote archive repositories were reconstructed and checked. Their salvage contained 1,439 byte-unique files, with 2,211 exact source-variant duplicates and 22 staging matches omitted. See `remote-archive-verification.json`. After comparison with the newer candidate, many salvaged files were already present at different paths and are not copied again.
- **`raw-media-inventory.json` contains 1,204 source-path entries (411,898,709 bytes total) with 1,172 distinct Git blob hashes.** None matched the original candidate baseline `4072851ad13536b3e65cbd7fecfe73d306038d32`; two of those hashes now appear only in the repository-list evidence screenshots added by PR #2. The remaining raw-media payloads are not included here and still require visual/privacy review. The inventory lists paths, sizes, and hashes only; hash differences do not decide whether a replacement is functionally equivalent or safe to publish.
- The candidate's `docs/IMAGE_SUMMARIES.md` inventories 1,296 images / 1,238 unique contents, but reports only seven visual summaries. Most entries still say visual summary pending. An inventory is not a replacement for the missing visual information.
- **66 shared paths differ** between the collected staging snapshot and the newer candidate. The newer candidate is retained. These differences are not automatically missing functionality. Review `shared-path-differences.json` and `preserved-source-variants.patch`; the patch contains alternative source edits against an older T44 baseline and must not be applied wholesale.

The counts above describe specific compared collections, not a claim that every differing legacy version is a required feature. Drafted handoff documents in the staging comparison are not automatically additional product requirements.

## Protected exclusions and outstanding work

The protected `artifacts/api-server/.local-data/natal-vault.json` was not inspected or uploaded. Private vault, credential/environment, and runtime chat/audit/applicant records remain excluded from the public review branch. Those exclusions require explicit owner/agent accounting; they are not duplicate proofs and do not authorize deletion of their source repositories.

This content audit does not verify application behavior or a passing build. It does not cover unknown uncommitted/unpushed work. At audit time, read-only access to 37 configured subrepl remotes failed host-key verification; a captured local merged-branch manifest preserves additional committed contributions, but does not prove every workspace's outstanding work is included. A later scoped update in issue #1 identified the 39th local ref and reported its admin-token changes already byte-identical in the candidate. That addresses the observed 38/39 local-ref discrepancy for that branch only; it does not resolve access to the configured remotes or verify other agents' pending work.

Each agent must compare its repository, branches, and pending work with the same proposed Grok-ready candidate, report source IDs and verification results in issue #1, and explicitly sign off. The owner must confirm the exact deletion list afterward.

**No source repository has been deleted by this review. The full migration is not verified complete.**
## Filename privacy

User-pasted text basenames in review metadata are replaced by stable neutral IDs. Original files remain in their source repositories; no pasted-text payloads are included in this review bundle.
## Personal-record diff privacy

Diff hunks that reproduce personal-record values are redacted from this public evidence file. The separate path/hash inventory preserves accounting; source records remain in their original repositories.
