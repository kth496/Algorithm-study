import java.io.BufferedReader
import java.io.InputStreamReader

fun main(args: Array<String>) {
    val MAXX: Int = 987654321
    val br = BufferedReader(InputStreamReader(System.`in`))

    fun test() = run {
        br.readLine()!!
                .split(" ")
                .map { it.toInt() }
    }

    val (n, m) = test()
    val adj = Array(n + 1) { IntArray(n + 1) { MAXX } }
//    val adj = Array(n + 1) { Array(n + 1) { MAXX } }

    repeat(m) {
        val (st, ed) = test()
        adj[st][ed] = 1
    }

    fun floyd() {
        for (k in 1..n) {
            for (i in 1..n) {
                for (j in 1..n) {
                    if (i == j) adj[i][j] = 0
                    else adj[i][j] = Math.min(adj[i][k] + adj[k][j], adj[i][j])
                }
            }
        }
    }

    floyd()

    var cnt = 0
    for (i in 1..n) {
        var ret = 0;
        for (j in 1..n) {
            if (Math.min(adj[i][j], adj[j][i]) == MAXX) break
            else ret++
        }
        if (ret == n) cnt++
    }
    println(cnt)
}
