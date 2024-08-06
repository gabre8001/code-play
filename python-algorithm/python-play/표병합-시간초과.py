
# 시간초과
def solution(commands):
    answer = []
    mat = []
    for i in range(51):
        temp = []
        for j in range(51):
            temp.append(["EMPTY",[[i,j]]])
        mat.append(temp)
 
    for c in commands:
        comm_arr = c.split(" ")
        comm_type = comm_arr[0]
        
        if comm_type == "UPDATE":
            if len(comm_arr) == 3:
                for i in range(51):
                    for j in range(51):
                        if mat[i][j][0] == comm_arr[1]:
                            mat[i][j][0] = comm_arr[2]
                continue
            comm_str = comm_arr[3]
            i = int(comm_arr[1])
            j = int(comm_arr[2])
            u_list = mat[i][j][1]
            for u in u_list:
                mat[u[0]][u[1]][0] = comm_str
            # print("UPDATE",mat[i][j])
        elif comm_type == "MERGE":
            i_1 = int(comm_arr[1])
            j_1 = int(comm_arr[2])
            i_2 = int(comm_arr[3])
            j_2 = int(comm_arr[4])
            if i_1 == i_2 and j_1 == j_2:
                continue
            str_1 = mat[i_1][j_1][0]
            if str_1 == "EMPTY" :
                str_1 = mat[i_2][j_2][0]
            # print("MERGE list",mat[i_1][j_1][1], mat[i_2][j_2][1])
            m_list = mat[i_1][j_1][1] + mat[i_2][j_2][1]
            # print("m_list", m_list)
            for m in m_list:
                mat[m[0]][m[1]][0] = str_1
                mat[m[0]][m[1]][1] = m_list
                # print("MERGE",mat[m[0]][m[1]])
        elif comm_type == "UNMERGE":
            i = int(comm_arr[1])
            j = int(comm_arr[2])
            comm_str = mat[i][j][0]
            m_list = mat[i][j][1]
            # print("UNMERGE",mat[i][j])
            for m in m_list:
                mat[m[0]][m[1]][0] = "EMPTY"
                mat[m[0]][m[1]][1] = [[m[0],m[1]]]
            mat[i][j][0] = comm_str
            # print("UNMERGE",i, j, comm_str, mat[1][1], mat[1][2], mat[2][1], mat[2][2])
        elif comm_type == "PRINT":
            i = int(comm_arr[1])
            j = int(comm_arr[2])
            answer.append(mat[i][j][0])

    # print(answer)
    return answer



if __name__ == "__main__":
    solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
    solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])
