package com.slo0ey.farmland

enum class Direction(private val direction: Int) {
    SOUTH(0), WEST(1), NORTH(2), EAST(3);

    fun toInt(): Int {
        return direction
    }

    fun rotate(time: Int): Direction {
        var degrees = (direction + time) % 4
        if (degrees < 0) degrees += 4

        return when(degrees) {
            0 -> SOUTH
            1 -> WEST
            2 -> NORTH
            else -> EAST
        }
    }
}
