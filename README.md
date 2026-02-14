# AIAssisted-Core

> **Archived** — Research project from October 2020. No longer maintained.

GPT-2 fine-tuning pipeline for automated code generation — built 8+ months before GitHub Copilot (June 2021).

## Context

In late 2020, we set out to build an AI-powered coding assistant by fine-tuning GPT-2 on source code. The vision was right — GitHub Copilot, Codeium, and others proved the market a year later — but the technology wasn't ready. GPT-2 124M was too small to produce reliable code output, and there was no funding ecosystem for AI developer tools yet. We shelved the project.

## Overview

Fine-tunes GPT-2 124M on source code and serves predictions via a FastAPI endpoint. Data collection, preprocessing (SentencePiece), fine-tuning, and inference in a single pipeline.

## Stack

Python, TensorFlow, FastAPI, Docker

## Authors

- [Joseph Goksu](https://github.com/josephgoksu) — ML pipeline and inference server
- [Azmi Mengu](https://github.com/azmimengu) — [AWS deployment stack](https://github.com/reaktif-io/AI-Assisted-AWS-Stack)
