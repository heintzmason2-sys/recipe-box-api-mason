2026-11-25: Anonymous GET /recipes → 200, returned all recipes including is_public=false items (e.g. secret hot sauce).

2026-11-25: Anonymous PATCH /recipes/3 → 200, title changed from "Secret family hot sauce" to "Totally not secret anymore hot sauce" with no authentication.

2026-11-25: Anonymous DELETE /recipes/3 → 204, secret recipe permanently deleted with no authentication; subsequent GET /recipes no longer shows id 3.