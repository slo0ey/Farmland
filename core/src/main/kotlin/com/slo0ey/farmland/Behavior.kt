package com.slo0ey.farmland

enum class Behavior {
    IDLE, MOVE, HOE;

    fun asAtlasKey(): String = this.toString().lowercase()
}
