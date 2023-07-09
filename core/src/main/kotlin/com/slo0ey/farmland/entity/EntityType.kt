package com.slo0ey.farmland.entity

enum class EntityType {
    PLAYER, UNKNOWN;

    fun toAtlasKey(): String = this.toString().lowercase()
}
