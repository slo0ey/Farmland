package com.slo0ey.farmland.system

import com.badlogic.gdx.scenes.scene2d.Event
import com.badlogic.gdx.scenes.scene2d.EventListener
import com.github.quillraven.fleks.Entity
import com.github.quillraven.fleks.IteratingSystem
import com.github.quillraven.fleks.World.Companion.family
import com.slo0ey.farmland.component.SpawnComponent
import com.slo0ey.farmland.event.MapUpdateEvent
import ktx.tiled.layer

class EntitySpawnSystem: EventListener, IteratingSystem(
    family = family { all(SpawnComponent) }
) {
    override fun onTickEntity(entity: Entity) {
        TODO("Not yet implemented")
    }

    override fun handle(event: Event?): Boolean {
        if (event is MapUpdateEvent) {
            val entityLayer = event.map.layer("entities")
            return true
        }
        return false
    }
}
