package com.slo0ey.farmland.system

import com.badlogic.gdx.graphics.OrthographicCamera
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer
import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer
import com.badlogic.gdx.maps.tiled.tiles.AnimatedTiledMapTile
import com.badlogic.gdx.scenes.scene2d.Event
import com.badlogic.gdx.scenes.scene2d.EventListener
import com.badlogic.gdx.scenes.scene2d.Stage
import com.github.quillraven.fleks.Entity
import com.github.quillraven.fleks.IteratingSystem
import com.github.quillraven.fleks.World.Companion.family
import com.github.quillraven.fleks.World.Companion.inject
import com.github.quillraven.fleks.collection.compareEntity
import com.slo0ey.farmland.component.ImageComponent
import com.slo0ey.farmland.event.MapUpdateEvent
import ktx.graphics.moveTo
import ktx.graphics.use
import ktx.math.vec2
import ktx.tiled.forEachLayer
import ktx.tiled.property

class RenderSystem(
    private val stage: Stage = inject("stage")
): EventListener, IteratingSystem(
    family = family { all(ImageComponent) },
    comparator = compareEntity { e1, e2 -> e1[ImageComponent].compareTo(e2[ImageComponent]) }
) {
    private val mapRenderer = OrthogonalTiledMapRenderer(null, 1/64f, stage.batch)
    private val orthoCamera: OrthographicCamera = stage.camera as OrthographicCamera
    private val bgLayers = mutableListOf<TiledMapTileLayer>()
    private val fgLayers = mutableListOf<TiledMapTileLayer>()

    override fun onTick() {
        super.onTick()

        with(stage) {
            viewport.apply()

            AnimatedTiledMapTile.updateAnimationBaseTime()
            mapRenderer.setView(orthoCamera)

            if (bgLayers.isNotEmpty()) {
                batch.use(orthoCamera.combined) {
                    bgLayers.forEach { layer ->
                        mapRenderer.renderTileLayer(layer)
                    }
                }
            }

            act(deltaTime)
            draw()

            if (fgLayers.isNotEmpty()) {
                batch.use(orthoCamera.combined) {
                    fgLayers.forEach { layer ->
                        mapRenderer.renderTileLayer(layer)
                    }
                }
            }

            orthoCamera.moveTo(vec2(100f, 115f))
        }
    }

    override fun onTickEntity(entity: Entity) {
        entity[ImageComponent].image.toFront()
    }

    override fun handle(event: Event?): Boolean {
        if (event is MapUpdateEvent) {
            mapRenderer.map = event.map
            bgLayers.clear()
            fgLayers.clear()
            event.map.forEachLayer<TiledMapTileLayer> { layer ->
                val z = layer.property<Int>("Z")
                if (z < 4) {
                    bgLayers.add(layer)
                } else {
                    fgLayers.add(layer)
                }
            }
            return true
        }
        return false
    }

    override fun onDispose() {
        mapRenderer.dispose()
    }
}
