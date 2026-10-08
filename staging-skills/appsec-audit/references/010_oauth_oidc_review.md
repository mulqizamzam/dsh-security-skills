# 010 — oauth_oidc_review

## trigger
- keywords: ["oauth", "oidc", "sso", "authorization code"]
- file_globs: ["**/oauth/**", "**/oidc/**", "**/sso/**"]
- regex: ["(?i)(oauth|oidc|openid|authorization_code|client_secret)"]
- ast: []

## severity
high

## intent
Review OAuth 2.0 / OIDC flows for the current best practice (RFC 9700 / OAuth 2.1).

## procedure
1. Reject implicit flow and ROPC.
2. Require PKCE (S256) for all public clients and confidential clients.
3. Require exact redirect_uri match; no wildcards, no open redirect.
4. Require state parameter (or use PKCE + nonce).
5. Validate id_token: signature, iss, aud, exp, nbf, nonce.
6. For confidential clients: prefer private_key_jwt or mTLS over client_secret.
7. Scope minimization; no wildcard scopes.
8. Token storage: access in memory, refresh in httpOnly cookie or secure storage.
9. Revocation + introspection endpoints available.

## checks
- [ ] No implicit flow
- [ ] PKCE S256 enforced
- [ ] Exact redirect_uri match
- [ ] state + nonce
- [ ] id_token fully validated
- [ ] Scopes least-privilege
- [ ] Refresh token rotation + reuse detection

## references
- RFC 6749, 6750, 7636, 9700
- OpenID Connect Core 1.0
- OAuth 2.0 Security Best Current Practice

## output
Flow diagram + findings table.
