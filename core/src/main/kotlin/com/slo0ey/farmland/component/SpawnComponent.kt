package com.slo0ey.farmland.component

import com.badlogic.gdx.math.Vector2
import com.github.quillraven.fleks.Component
import com.github.quillraven.fleks.ComponentType
import com.slo0ey.farmland.entity.EntityType
import ktx.math.vec2

data class SpawnConfig(
    val type: EntityType
)

class SpawnComponent(
    val entityType: EntityType,
    val location: Vector2 = vec2()
): Component<SpawnComponent> {

    override fun type() = SpawnComponent

    companion object: ComponentType<SpawnComponent>()
}
