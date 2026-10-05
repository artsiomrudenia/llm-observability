# ADR-0001: Initial Architecture

- Date: 05/10/2026
- Status: Accepted

## Context

The project needs a public baseline for collecting and exposing LLM telemetry in Kubernetes environments.

## Decision

Start with a lightweight FastAPI service and provide standardized container + Kubernetes delivery artifacts.

## Consequences

- Clear extension path for metrics, traces, and dashboards
- Immediate CI validation with tests and image build
