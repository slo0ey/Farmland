package com.slo0ey.farmland.component

import com.badlogic.gdx.scenes.scene2d.ui.Image
import com.github.quillraven.fleks.*

class ImageComponent : Component<ImageComponent>, Comparable<ImageComponent> {
    lateinit var image: Image

    override fun compareTo(other: ImageComponent): Int {
        val yDiff = other.image.y.compareTo(image.y)
        return if (yDiff != 0) {
            yDiff
        } else {
            other.image.x.compareTo(image.x)
        }
    }

    override fun type() = ImageComponent

    companion object : ComponentType<ImageComponent>()
}
