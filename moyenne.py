def moyenne(notes):
    return sum(notes)/len(notes)

def note_max(notes):
    return max(notes)
def mediane(notes):
    tri=sorted(notes)
    n=len(tri)
    return tri[n//2]

notes=[12,15,9,18]
print("Moyenne:",moyenne(notes))
print("note maximale:",note_max(notes))
print("médiane:",mediane(notes))

print("hello")
