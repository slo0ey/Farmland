package com.slo0ey.farmland.component

import com.github.quillraven.fleks.Component
import com.github.quillraven.fleks.ComponentType

class AnimationComponent: Component<AnimationComponent> {
    override fun type() = AnimationComponent

    companion object : ComponentType<AnimationComponent>()
}
