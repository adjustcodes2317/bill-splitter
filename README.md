# Bill Splitter

A command line Python program that helps groups of people split a bill fairly — either equally or based on what each person ordered. It also tells you exactly who owes money to whom so there is no confusion at the end.

---

## The Problem

When a group of friends or roommates go out to eat or order food together, splitting the bill at the end is always a hassle. There are usually two situations:

**Situation 1** — Everyone ordered roughly the same thing, so splitting equally makes sense. But doing the math manually, especially with a big group, takes time and someone always gets it wrong.

**Situation 2** — People ordered very different things. One person had just a drink, another had a full meal. Splitting equally in this case feels unfair. You need to calculate each person's individual share, which gets confusing fast.

On top of that, even after calculating the shares, the question remains — who actually pays who? This program solves all of that in seconds.

---

## What It Does

The program gives you two options:

**Option 1 — Equal Split**
You enter the total bill amount and the number of people. The program divides the total equally, prints how much each person needs to pay, and then shows who owes that amount to the person who originally paid.

**Option 2 — Custom Split**
You enter each person's name and the amount they individually ordered. The program adds everything up, shows each person's share, and then calculates who owes money and who should get money back based on the group average.

---

## How to Run

Make sure Python 3 is installed on your computer. You can check by running:

```
python --version
```

Then run the program:

```
python bill_splitter.py
```

No extra libraries or installations needed. It runs on plain Python.

---

## Example Usage

**Equal Split:**
```
welcome to bill splitter
1. split equally
2. split by what each person ordered
3. exit

enter choice : 1
enter total bill : 900
how many people : 3
enter name : rahul
enter name : priya
enter name : amit

result --
rahul has to pay 300.0
priya has to pay 300.0
amit has to pay 300.0

who owes whom --
priya owes rahul --> 300.0
amit owes rahul --> 300.0
```

**Custom Split:**
```
enter choice : 2
how many people : 3
name : rahul
how much did they order : 450
name : priya
how much did they order : 250
name : amit
how much did they order : 200

result --
total bill is 900.0
rahul pays 450.0
priya pays 250.0
amit pays 200.0

who owes whom --
rahul should get back 150.0 from the group
priya owes 50.0 to the group
amit owes 100.0 to the group
```

---

## Project Structure

```
bill-splitter/
│
├── bill_splitter.py      # main program
├── README.md             # this file
└── Project_Report.md     # full project report
```

---

## Requirements

- Python 3
- No external libraries needed

---

## Author

[Your Name] — [Your Roll No] — AI / ML Basics Course

