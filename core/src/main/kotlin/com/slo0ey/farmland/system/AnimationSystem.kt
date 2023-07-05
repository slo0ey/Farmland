package com.slo0ey.farmland.system

import com.github.quillraven.fleks.Entity
import com.github.quillraven.fleks.IteratingSystem
import com.github.quillraven.fleks.World.Companion.family
import com.slo0ey.farmland.component.AnimationComponent
import com.slo0ey.farmland.component.ImageComponent

class AnimationSystem(

): IteratingSystem(
    family = family { all(ImageComponent, AnimationComponent) }
) {
    override fun onTickEntity(entity: Entity) {

    }
}
