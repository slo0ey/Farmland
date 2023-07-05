package com.slo0ey.farmland.screen

import com.badlogic.gdx.graphics.g2d.TextureAtlas
import com.badlogic.gdx.scenes.scene2d.Stage
import com.badlogic.gdx.scenes.scene2d.ui.Image
import com.badlogic.gdx.utils.Scaling
import com.badlogic.gdx.utils.viewport.ExtendViewport
import com.github.quillraven.fleks.World
import com.github.quillraven.fleks.world
import com.slo0ey.farmland.Behavior
import com.slo0ey.farmland.Direction
import com.slo0ey.farmland.component.AnimationComponent
import com.slo0ey.farmland.component.ImageComponent
import com.slo0ey.farmland.entity.EntityType
import com.slo0ey.farmland.system.AnimationSystem
import com.slo0ey.farmland.system.RenderSystem
import ktx.app.KtxScreen
import ktx.log.logger

class GameScreen: KtxScreen {
    private val stage: Stage = Stage(ExtendViewport(16f, 9f))
    private val entityAtlas: TextureAtlas = TextureAtlas("sprite/entity.atlas")
    private val world: World = world {
        injectables {
            add("stage", stage)
            add("EntityAtlas", entityAtlas)
        }

        components {
            onAdd(ImageComponent) { entity, component ->
                stage.addActor(component.image)
            }
            onRemove(ImageComponent) { entity, component ->
                stage.root.removeActor(component.image)
            }
        }

        systems {
            add(AnimationSystem())
            add(RenderSystem())
        }
    }

    override fun show() {
        LOG.debug { "GameScreen: show!" }

        world.entity {
            it += ImageComponent().apply {
                image = Image().apply {
                    setSize(2f, 2f)
                    setScaling(Scaling.fill)
                }
            }
            it += AnimationComponent(EntityType.PLAYER).apply {
                nextAnimation(Behavior.HOE, Direction.SOUTH)
            }
        }
    }

    override fun resize(width: Int, height: Int) {
        stage.viewport.update(width, height, true)
    }

    override fun render(delta: Float) {
        world.update(delta)
    }

    override fun dispose() {
        stage.dispose()
        entityAtlas.dispose()
        world.dispose()
    }

    companion object {
        private val LOG = logger<GameScreen>()
    }
}
