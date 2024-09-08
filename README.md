# VIT AP Classroom Occupancy Details

> [!IMPORTANT]
> The data used(i.e. `cxl.csv` is not up to date, and used the time slot configuration of `WIN SEM 23-24 Freshers`, use this data only for prototyping)


Use `time_slots.json` for the following format:
```bash

{
    "10:00-10:50": {
        "CB": [
            "113",
            "214",
            "G13",
            "109",
            "422",
            "314",
            "226",
            "307",
            "114",

            ...

```

Use `output4.json` for the following format of json:

```json
{
    "CB": {
        "F1": [
            {
                "course_code": "STS3006",
                "course_title": "Basic Competitive Coding - I",
                "employee_name": "ARIVARASAN A",
                "room_number": "307",
                "slot_times": {
                    "F1": "10:00-10:50",
                    "TF1": "08:00-08:50"
                }
            },
            {
                "course_code": "STS3007",
                "course_title": "Advanced Competitive Coding - I",
                "employee_name": "Prof. Bhavya",
                "room_number": "405",
                "slot_times": {
                    "F1": "10:00-10:50",
                    "TF1": "08:00-08:50"
                }
            },

        ...

```