package com.slo0ey.farmland.component

import com.badlogic.gdx.graphics.g2d.Animation
import com.badlogic.gdx.graphics.g2d.Animation.PlayMode
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable
import com.github.quillraven.fleks.Component
import com.github.quillraven.fleks.ComponentType
import com.slo0ey.farmland.Behavior
import com.slo0ey.farmland.Direction
import com.slo0ey.farmland.entity.EntityType

class AnimationComponent(
    var entityType: EntityType,
    var stateTime: Float = 0f,
    var playMode: PlayMode = PlayMode.LOOP
): Component<AnimationComponent> {
    lateinit var animation: Animation<TextureRegionDrawable>
    var nextAnimation: String = NO_ANIMATION
        private set

    fun nextAnimation(behavior: Behavior) {
        nextAnimation = "${entityType.asAtlasKey()}/${behavior.asAtlasKey()}"
    }

    fun nextAnimation(behavior: Behavior, direction: Direction) {
        nextAnimation = "${entityType.asAtlasKey()}/${behavior.asAtlasKey()}/${direction.asInt()}"
    }

    fun clearAnimation() {
        nextAnimation = NO_ANIMATION
    }

    fun isAnimationFinished() = animation.isAnimationFinished(stateTime)

    override fun type() = AnimationComponent

    companion object : ComponentType<AnimationComponent>() {
        const val NO_ANIMATION = ""
    }
}
