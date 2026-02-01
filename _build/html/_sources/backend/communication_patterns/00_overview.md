# Communication Patterns

How backend services and clients communicate: synchronous request/response, streaming, and asynchronous messaging.

## Core Modes
- **HTTP request/response (sync)** -> REST, GraphQL, RPC, idempotency, timeouts.
- **Server-Sent Events (SSE)** -> one-way streaming updates over HTTP.
- **WebSockets** -> bidirectional realtime channels for low-latency state sync.
- **Async messaging** -> queues, pub/sub, background jobs, decoupled workflows.

## Design Considerations
- **Retries & idempotency** -> safe replays, backoff, circuit breakers.
- **Backpressure** -> flow control, buffering, slow consumers.
- **Delivery semantics** -> at-most/at-least/exactly-once, deduplication.
- **Ordering** -> per-key ordering, partitioning, fan-out.

## When to Use What
- **Request/response** for CRUD and transactional flows.
- **SSE** for many listeners that need live updates.
- **WebSockets** for interactive realtime collaboration.
- **Async messaging** for long-running or bursty workloads.
