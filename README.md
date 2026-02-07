# Departure PI
- Real-time Vienna public transport departures on a Raspberry Pi Zero W with a
16x2 LCD, powered by the Wiener Linien open data API.

## Overview
- Fetches real-time departure data from the Wiener Linien API for a configured
stop.
- Displays the next two departures with line, direction, countdown, and a real-
time indicator on a 16x2 character LCD. Refreshes every 30 seconds.

## Architecture
- The application is split into layers: a main loop that loads config and
coordinates refreshes, an API client that fetches and parses departure data, and
a display module that formats output for the hardware.

```
main.py                Entry point, config loading, refresh loop
fetch_data.py          API client for Wiener Linien real-time departures
display_data_lcd.py    Display abstraction, formats data for 16-char rows
LCD1602.py             I2C hardware driver for LCD1602 module
config.json            Stop ID configuration (not committed)
```

## Display Format
- Each row is formatted to exactly 16 characters:

```
10A  Kagra   3
35A  Spit   12*
```

`LINE DIRECTION MIN` — direction is truncated to fit. `*` indicates scheduled
time (no real-time data available).

## Hardware
- Raspberry Pi Zero W
- Waveshare LCD1602 RGB Module (I2C)
- I2C wiring (SDA/SCL)

## Getting Started
- Getting started:
```bash
git clone https://github.com/VSharon1/departure-pi.git
cd departure-pi
pip install requests smbus
cp config.example.json config.json
```

- Set your stop ID in `config.json`, then run:
```bash
python main.py
```

- Find your stop ID: [WL RBL/StopId Search](https://till.mabe.at/rbl/)

## Roadmap
- [ ] Hardware/software setup documentation
- [ ] Scheduled display power on/off (cron + transistor circuit)
- [ ] NFC tag trigger for on-demand activation

## Built With
- Python 3, Raspberry Pi OS Lite
- [Wiener Linien Real-Time API](https://www.wienerlinien.at/ogd_realtime/monitor)

## Acknowledgments
- **3D Case** — [Raspberry Pi Zero + Waveshare LCD 1602 Case](https://www.thingiverse.com/thing:5952644)
by [bapplegate513](https://www.thingiverse.com/bapplegate513)
- **Stop ID Lookup** — [WL RBL/StopId Search](https://till.mabe.at/rbl/) by
[.mabe](https://mabe.at)