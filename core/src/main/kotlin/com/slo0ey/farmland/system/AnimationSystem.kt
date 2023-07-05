package com.slo0ey.farmland.system

import com.badlogic.gdx.graphics.g2d.Animation
import com.badlogic.gdx.graphics.g2d.TextureAtlas
import com.badlogic.gdx.scenes.scene2d.utils.TextureRegionDrawable
import com.github.quillraven.fleks.Entity
import com.github.quillraven.fleks.IteratingSystem
import com.github.quillraven.fleks.World.Companion.family
import com.github.quillraven.fleks.World.Companion.inject
import com.slo0ey.farmland.component.AnimationComponent
import com.slo0ey.farmland.component.AnimationComponent.Companion.NO_ANIMATION
import com.slo0ey.farmland.component.ImageComponent
import ktx.app.gdxError
import ktx.collections.toGdxArray

class AnimationSystem(
    private val atlas: TextureAtlas = inject("EntityAtlas")
): IteratingSystem(
    family = family { all(ImageComponent, AnimationComponent) }
) {
    private val cachedAnimations = mutableMapOf<String, Animation<TextureRegionDrawable>>()

    override fun onTickEntity(entity: Entity) {
        val imgComp = entity[ImageComponent]
        val aniComp = entity[AnimationComponent]

        with(imgComp) {
            image.drawable = if (aniComp.nextAnimation != NO_ANIMATION) {
                aniComp.run {
                    animation = loadAnimation(nextAnimation)
                    clearAnimation()
                    stateTime = 0f
                    animation.playMode = playMode
                    animation.getKeyFrame(0f)
                }
            } else {
                aniComp.run {
                    stateTime += deltaTime
                    animation.playMode = playMode
                    animation.getKeyFrame(stateTime)
                }
            }
        }
    }

    private fun loadAnimation(animation: String): Animation<TextureRegionDrawable> {
        return cachedAnimations.getOrPut(animation) {
            val regions = atlas.findRegions(animation)
            if (regions.isEmpty) {
                gdxError("No Textures for $animation")
            }
            val duration = 1f / regions.size
            val keyFrames = regions.map { TextureRegionDrawable(it) }
            Animation(duration, keyFrames.toGdxArray())
        }
    }
}
