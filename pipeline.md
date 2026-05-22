# RT-Deepdive — Project Pipeline

## Repository Layout

```
RT-deepdive/
├── pipeline.md                        ← this file
├── CLAUDE.md                          ← AI handoff protocol
│
├── engine/                            ← Python ray tracing engine (importable package)
│   ├── __init__.py
│   ├── core.py                        ← Data models: Ray, Material
│   ├── intersection.py                ← Ray-surface intersection (Möller–Trumbore)
│   └── parsers/                       ← Mesh I/O (to be populated)
│       └── obj_parser.py              ← Wavefront .obj loader (planned)
│
├── notebooks/
│   └── ray_tracing_sandbox.ipynb      ← Exploratory scratchpad, imports engine/
│
└── docs/                              ← Static HTML knowledge base (no build step)
    ├── index.html                     ← Reflection & Refraction reference
    ├── notes.html                     ← Research Notes (Electromagnetism & Maxwell)
    ├── diffraction.html               ← Diffraction & Scattering notes
    ├── assets/                        ← Images, diagrams (gitkeep placeholder)
    └── fundamentals/                  ← Deep-dive concept pages
        └── wavefront-obj.html         ← Wavefront .obj format & parser conventions
```

---

## Module Responsibilities

| Path | Role |
|---|---|
| `engine/core.py` | `Ray` and `Material` dataclasses — the shared data contract for every other module |
| `engine/intersection.py` | `Surface` geometry and `ray_triangle_intersect` (Möller–Trumbore) |
| `engine/parsers/obj_parser.py` | Load `.obj` files → populate vertex/face/normal lists consumed by `Surface` |
| `notebooks/` | Prototype and visualise; always imports from `engine/`, never duplicates logic |
| `docs/` | Human-readable theory reference; pure HTML + MathJax, no framework |

---

## Dependency Flow

```
docs/          (standalone, no imports)

engine/core.py
    ↑
engine/intersection.py   (imports core)
    ↑
engine/parsers/obj_parser.py   (produces vertex/face data fed into Surface)
    ↑
notebooks/   (imports engine.*, drives end-to-end experiments)
```

---

## Naming & Placement Rules

- **New engine logic** (shaders, BRDFs, scene graph) → `engine/<module>.py`
- **New I/O / file parsers** → `engine/parsers/<format>_parser.py`
- **New theory documentation** → `docs/fundamentals/<topic>.html`
- **No `src/` directory** — the engine package root is `engine/`
- **No duplicate logic** between notebooks and engine — notebooks call engine functions

---

## Current Implementation Status

| Component | Status |
|---|---|
| `Ray`, `Material` models | Stub (interface defined, body pending) |
| `Surface`, `ray_triangle_intersect` | Stub (Möller–Trumbore pending) |
| `ObjParser` | Planned — Step 1 pending approval |
| Docs site | Live — 4 pages |
