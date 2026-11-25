

## Rally Cam Project

| Field | My project |
|---|---|
| Domain | Synthetic two-player tennis video |
| Decision unit | One video frame |
| Classes | active, passive, nobody |
| Labels that already exist | Blue and orange player bounding boxes |
| Label I will generate | Which player is closer to the ball, if either is within 150 pixels |
| Match rule | IoU ≥ 0.5 against an existing player box |
| Trainable statuses | `matched` and `no_positive` |
| Split unit | One video ID, not one frame |
| Model input | 12 channels: 3 RGB frames plus 3 candidate masks |
| Application metric | correct, missed, wrong instance, false positive |
| Audit size | 5 manually inspected frames from the 30-frame sample |

## Project facts

- Image size: 640 × 360.
- Source video ID: `rally_a`.
- Frame rate: 10 FPS.
- Frames: 0 through 29.
- Blue player box at frame `f`: `(80+4f, 120, 160+4f, 280)`.
- Orange