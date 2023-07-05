package com.slo0ey.farmland

enum class Direction(private val direction: Int) {
    SOUTH(0), WEST(1), NORTH(2), EAST(3);

    fun asInt(): Int {
        return direction
    }

    operator fun inc(): Direction {
        return when((direction + 1) % 4) {
            1 -> WEST
            2 -> NORTH
            3 -> EAST
            else -> SOUTH
        }
    }

    operator fun plus(rotate: Int): Direction {
        return when((direction + rotate) % 4) {
            1 -> WEST
            2 -> NORTH
            3 -> EAST
            else -> SOUTH
        }
    }

    operator fun dec(): Direction {
        return when((direction + 3) % 4) {
            1 -> WEST
            2 -> NORTH
            3 -> EAST
            else -> SOUTH
        }
    }

    operator fun minus(rotate: Int): Direction {
        return when((direction - rotate) % 4 + 4) {
            1 -> WEST
            2 -> NORTH
            3 -> EAST
            else -> SOUTH
        }
    }
}
