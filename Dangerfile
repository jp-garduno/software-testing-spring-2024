# Checks some basic commit message style:
#   - The title (first line) is not longer than 50 characters.
#   - The title and body have to be separated by newline.
#   - The description has minimum 5 characters.
#   - Each description line is not longer than 72 characters.

commitIssues = []

for commit in git.commits
  (subject, empty_line, *body) = commit.message.split("\n")

  commitIssues << "Commit title is too long: &lt;#{subject}&gt;" if subject.length > 50
  commitIssues << "Commit title and body are not separated: &lt;#{subject}&gt;" if empty_line && empty_line.length > 0

  description_length = body.length > 0 ? body.first.length : 0
  commitIssues << "Please include a description for commit &quot;#{subject}&quot;" if (description_length < 5)

  for line in body
    commitIssues << "Commit text lines are too long: &lt;#{subject}&gt;" if line.length > 72
  end
end

for issue in commitIssues
  fail issue
end
