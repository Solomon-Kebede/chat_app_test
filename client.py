#!/usr/bin/env python3

import cmd

class ChatClient(cmd.Cmd):
	prompt = '> '
	output_prompt = '< '
	def onecmd(self, line):
		if line == 'EOF' or line == 'exit':
			return cmd.Cmd.onecmd(self, 'EOF')
		else:
			# result = eval(line)
			# print(f'{ChatClient.output_prompt}{result}')
			print(f'{ChatClient.output_prompt}"{line}"')
	def do_EOF(self, line):
		return True


if __name__ == '__main__':
	ChatClient().cmdloop()