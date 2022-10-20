from oscar import Project, Author, Blob, Commit, Tree
import base64

import json
repo = Project('jhonatancunha_quizUTFPR')

file = open("data.csv", "w")

print("Salvando...")

file.write("repo,filename,author,authored_at,committer,committed_at,sha,message,blob\n")

for author in repo.author_names:
	name, email = str(author)[1:].split('<')	
	name_email = f'%s <%s' % (name[1:-1], email[:-1]) 

	print("Salvando informacoes de: ", name_email)
	person = Author(name_email)
	
	for c in person.commit_shas:
		commit = Commit(c)
		tree = Tree(commit.tree.sha)
		message = base64.b64encode(commit.message)
		projectNames = [str(x) for x in commit.project_names]
		
		for element in tree:
			mode, filename, sha = element			
			blob = Blob(sha)
			blobContent = None
			try:
				blobContent = json.dumps(str(blob.data)).encode('utf-8')
				blobContent64 = base64.b64encode(blobContent)	
			except:
				pass

			if("." in str(filename)):
				line = [str(" ".join(projectNames)),str(filename, "UTF-8"), str(commit.author, "UTF-8"), str(commit.authored_at), str(commit.committer, "UTF-8"), str(commit.committed_at), str(commit.sha), str(message), str(blobContent64)]
				
				file.write(",".join(line) + "\n")
	

print("Salvo")
file.close()

