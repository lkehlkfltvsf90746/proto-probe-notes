# Invalidated finding: nodejs/http-parser oversized chunk input

> **Status: invalidated on 2026-07-21. Not a confirmed vulnerability or CVE.**
> A correction was prepared for the CNA request submitted on 2026-07-15.

## Original observation

The reproducer declared a chunk size of `0xFFFFF`, supplied only a few dozen
bytes, and observed that `http_parser_execute()` delivered those bytes through
the body callback while retaining a non-zero `content_length`.

## Why the original conclusion was wrong

1. `http_parser` is a streaming parser. Callers continue feeding data received
   on the same TCP connection and signal EOF with a zero-length call.
2. A `0xFFFFF` chunk is not complete until exactly that amount of chunk-data,
   its terminating CRLF, and the later zero-sized chunk have been received.
3. Bytes that happen to spell `GET /admin` have no message-boundary meaning
   while the declared chunk body is incomplete; they are chunk-data.
4. RFC 9112 chunk extensions use a semicolon. `FFFFF F` is not the valid
   extension claimed in the original report.
5. The harness included only one parser. It did not show a backend parsing the
   same bytes as a second request, so it did not establish CWE-444.

The original `HPE_OK` result meant that the bytes supplied in that invocation
were consumed without a syntax error. It did not mean the HTTP message was
complete. The remaining `content_length` was evidence of incomplete input,
not evidence of a parser boundary vulnerability.

## Correct lesson

Parser state is an observation, not an impact oracle. A request-smuggling claim
requires a concrete differential between two components on a complete byte
stream, plus a deployment model that preserves the disagreement. Future tests
will include fragmented input, EOF, valid syntax, strict negative controls,
and a second parser or real proxy/backend harness.

This note is retained to make the correction visible and prevent the same
false positive from being reported again.
