## trigger
- keywords: ["websocket", "ws", "wss"]
- file_globs: ["**/ws/**", "**/socket/**"]
- regex: ["(?i)(WebSocket|socket\\.io|ws://)"]
- ast: []

## severity
high

## intent
Harden WebSocket endpoints.

## procedure
1. WSS only.
2. Authn on handshake; token in subprotocol or cookie, not query.
3. Origin check on handshake.
4. Per-message authz.
5. Rate limit messages.
6. Message size limit.
7. Heartbeat + idle timeout.
8. No CSRF-able state change without token.

## checks
- [ ] WSS
- [ ] Authn on handshake
- [ ] Origin check
- [ ] Rate limit
- [ ] Size limit
- [ ] Idle timeout

## references
- OWASP WebSocket Security
- RFC 6455

## output
Findings + handshake middleware.
```

---
