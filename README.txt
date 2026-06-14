AccessTwin v3 — Guided + Smooth

WHAT CHANGED
- Audio-driven guided walkthrough with spotlight focus, auto-scroll, glow, and section cues.
- During narration, page controls and sliders are locked so the walkthrough stays coherent.
- Pause the narration to unlock the full interface and manually explore or drag sliders.
- Scenario Studio, Value Frontier, and Market Network sliders now update in place with requestAnimationFrame instead of re-rendering the full page.
- Larger slider hit area and thumb for smoother mouse and touch interaction.
- Existing 8 audio clips remain compatible; no audio regeneration is required.

RUN
1. Keep the HTML, generate_audio_accesstwin.py, and the audio folder together.
2. If audio files already exist as audio/section_0.mp3 through audio/section_7.mp3, reuse them.
3. Otherwise run: python generate_audio_accesstwin.py
4. Serve locally: python -m http.server 8000
5. Open: http://localhost:8000/AccessTwin_Global_Pricing_Decision_Room.html
