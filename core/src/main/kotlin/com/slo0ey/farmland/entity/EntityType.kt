package com.slo0ey.farmland.entity

enum class EntityType {
    PLAYER, UNKNOWN;

    fun asAtlasKey(): String = this.toString().lowercase()
}
