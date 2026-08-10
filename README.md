# lkehlkfltvsf90746 · Protocol Parser Research Notes

This repository records protocol-parser research, including candidates that were
invalidated during verification and **reproductions of public CVEs**.

A submitted report is not a vulnerability until the technical claim is
independently supported. A CNA receipt is not validation.

## Current status

| Item | Status |
|---|---|
| Original confirmed vulnerabilities with CVE | **none yet** |
| Original reports with vendor fix/ack | [smolrtsp#58](https://github.com/OpenIPC/smolrtsp/issues/58) **fixed** ([PR#59](https://github.com/OpenIPC/smolrtsp/pull/59)); [hiredis#1333](https://github.com/redis/hiredis/issues/1333) ack + [PR#1334](https://github.com/redis/hiredis/pull/1334); [libhv#851](https://github.com/ithewei/libhv/issues/851) + [PR#854](https://github.com/ithewei/libhv/pull/854) |
| Related reports | [libhv#852](https://github.com/ithewei/libhv/issues/852) + [PR#853](https://github.com/ithewei/libhv/pull/853) |
| Invalidated candidates | http-parser incomplete-chunk claim (2026-07-21) |
| Known-CVE reproductions | CVE-2026-54387 Tinyproxy (tool validation only) |


## Layout

```
reports/
  http-parser-chunk-size-smuggling.md   # invalidated candidate (audit trail)
  reproduction/
    CVE-2026-54387-tinyproxy.md         # known CVE lab notes
  _template.md                          # original-finding template
lab/
  run_repro_check.py                    # loopback-only payload driver
```

## Research standard

A future **original** finding must include:

- a specification or documented implementation invariant;
- a minimal reproducer and a valid negative control;
- two implementations or components that disagree when the claim depends on a
  parser differential;
- complete, EOF, and fragmented-input tests where relevant;
- an impact statement supported by the harness rather than assumed from parser
  state alone.

## Related

- [http-framing-diff](https://github.com/lkehlkfltvsf90746/http-framing-diff) --framing_diff harness
- [http11-parser-corpus](https://github.com/lkehlkfltvsf90746/http11-parser-corpus)
- [traffic-analyzer](https://github.com/lkehlkfltvsf90746/traffic-analyzer)

Only test systems you own or are explicitly authorized to assess.
