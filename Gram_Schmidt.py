# import numpy as np

# def MSA(vectora,vectorb):
#     return np.dot(vectora,vectorb)
# def size(vector):
#     return np.sum(vector**2)


# def orthogonal_basis(vectors):
#     vectors = vectors.astype('float64')
#     vectors_output = np.asarray([vectors[0]])
    
#     for i in range(1,len(vectors)):
#         re = vectors[i]
#         for j in range(i):
#             re -= MSA(vectors[i],vectors_output[j]) * vectors_output[j] / size(vectors_output[j])
#         vectors_output = np.append(vectors_output,[re],axis = 0)
#     return vectors_output

# vectors = np.asarray([[4,1,3,-1],[2,1,-3,4],[1,0,-2,7],[6,2,9,-5]])

# basis = orthogonal_basis(vectors)
# for i in range(len(basis)):
#     for j in range(len(basis[i])):
#         basis[i][j] /= size(basis[i][j])
# print(basis)


import numpy as np 


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - np.sum( np.dot(v,b)*b  for b in basis )
        if (w > 1e-10).any():
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)

u = np.array([[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]])

basis = gram_schmidt(u)
# for i in range(len(basis)):
#     for j in range(len(basis[i])):
#         basis[i][j] /= size(basis[i][j])
print(basis)