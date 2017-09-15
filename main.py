#! /usr/bin/env python3
import sys
import argparse
from formula import LogicFormula

parser = argparse.ArgumentParser(description="Manipulate logical formulas")
parser.add_argument("command", choices=["evaluate", "table", "digraph", "infix", "postfix", "prefix"], 
	help="the action that should be performed on given formula. Commands are documented in the README.")
parser.add_argument("--format", default="infix", choices=["infix", "prefix", "postfix"], help="Input format of the formula.")
parser.add_argument("--values", metavar="vals", type=(lambda x: int(x, 2)), help="Values for variables used in the formula, in alphabetical order.")
parser.add_argument("formula", help="the formula to work with")

args = parser.parse_args()
formula = None
try:
	formula = LogicFormula(args.format, args.formula)
except Exception as e:
	print("Formula parse error:", file=sys.stderr)
	print(e, file=sys.stderr)
	sys.exit(1)

command = args.command
if command == "digraph":
	print(formula.digraph())
elif command == "table":
	formula.generate_evaluation_table()
elif command == "evaluate":
	if len(sys.argv) < 4: 
		print("evaluate usage: formula command values")
		sys.exit(1)
	print(formula.evaluate_with_bitset(args.values))
elif command == "infix":
	print(formula.infix())
elif command == "postfix":
	print(formula.postfix())
elif command == "prefix":
	print(formula.prefix())