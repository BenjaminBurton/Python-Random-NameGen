# Python-Random-NameGen

## EC2 Random Name Generator

This is my project for graduation! I made a Python script to make random names for EC2 instances in AWS. It’s for a shared AWS thing where departments need unique names so people know who owns what.

## What It Does

- **Advanced**: Only works for Marketing, Accounting, or FinOps depts. If you type something else, it says "nope". Works with big or small letters.

## Files

- `advanced_ec2_names.py` - Checks depts

## How to Run

1. SSH into your EC2 (I used Amazon Linux 2), but for sake of time this will be in terminal
2. Run them with `python3 filename.py`
3. Type how many names and the dept when it asks

## Example

If I run `python3 complex_ec2_names.py`:
