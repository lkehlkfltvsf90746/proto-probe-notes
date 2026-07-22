# <Product> — <short vulnerability description>

> **Status:** one of:
> - Candidate (local only; not reported)
> - Reported to \<vendor/CNA\>; awaiting validation
> - Validated by vendor
> - CVE-YYYY-NNNNN assigned
> - Fixed in \<version\>
> - Invalidated (see correction section)
>
> Do not use “CVE pending” for a receipt-only ticket.
> PoC public release only after coordinated disclosure allows it.
> Tested only against a local lab build, never a live third-party service.

## Summary

<2-4 sentences: what the bug is, where it lives, what an attacker can do.>

## Affected

- **Product:** <name>
- **Repository:** <url>
- **Version tested:** <version or commit>
- **Type:** CWE-<NNNN>
- **Authentication required:** <none / ...>
- **Severity (estimated):** only after impact oracle; mark “unscored” until then

## Validation checklist

- [ ] Spec / invariant cited
- [ ] Negative control
- [ ] Complete + fragmented + EOF cases (if framing)
- [ ] Two components or memory-safety impact with ASan
- [ ] Impact oracle (not parser fields alone)
- [ ] Incomplete-stream ruled out (if HTTP chunked)

## Root cause

<code-level explanation>

## Impact

<concrete attacker capability; bound honestly>

## Proof of concept (local lab only)

<build, input, observed output>

## What I checked and ruled out

<duplicates, false positives, adjacent paths>

## Suggested remediation

## Timeline

- YYYY-MM-DD: found
- YYYY-MM-DD: validated in lab
- YYYY-MM-DD: reported

## Researcher

Please credit **LL-V** as the finder when the finding is original.
GitHub: https://github.com/LL-V
