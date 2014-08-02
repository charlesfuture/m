formatter = "%s %s %s %s"
#print formatter %(1, 2, 3, 4)
print formatter %('one', 'two', 'three', 'four')
print formatter %(formatter, formatter, formatter, formatter)
print formatter %("I had this thing",
				"that you could type up right",
				"but it didn't sing",
				"so I said goodnight.")
print formatter