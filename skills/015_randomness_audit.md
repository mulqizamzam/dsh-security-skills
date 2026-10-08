## trigger
- keywords: ["random", "prng", "entropy", "nonce", "uuid"]
- file_globs: ["**/rand/**", "**/nonce/**"]
- regex: ["(?i)(math\\.random|rand\\(\\)|random\\.randint|Random\\(|srand|mt19937)"]
- ast: ["Call:rand", "Call:random"]

## severity
critical

## intent
Ensure all security-relevant randomness comes from a CSPRNG.

## procedure
1. Reject: `Math.random`, `rand()`, `random.randint` for security use, Mersenne Twister, LCG, time-seeded.
2. Approve: `crypto.randomBytes`, `secrets.token_bytes`, `crypto.getRandomValues`, `getrandom(2)`, `/dev/urandom`, `BCryptGenRandom`.
3. Verify nonce uniqueness for GCM/CTR: random 96-bit nonces are safe up to 2^32 messages; above that use counter.
4. Verify token entropy ≥128 bits for session/reset/API keys.
5. Verify no modulo bias in bounded ranges (use rejection sampling).
6. Verify seeding not from predictable source.

## checks
- [ ] CSPRNG for all security randomness
- [ ] ≥128-bit tokens
- [ ] Nonce uniqueness strategy documented
- [ ] No modulo bias
- [ ] No time-based seeding

## references
- NIST SP 800-90A/B/C
- OWASP Cryptographic Storage Cheat Sheet

## output
Findings + replacement snippet.

---
