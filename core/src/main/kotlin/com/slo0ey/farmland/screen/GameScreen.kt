package com.slo0ey.farmland.screen

import com.badlogic.gdx.graphics.Texture
import com.badlogic.gdx.graphics.g2d.TextureRegion
import com.badlogic.gdx.scenes.scene2d.Stage
import com.badlogic.gdx.scenes.scene2d.ui.Image
import com.badlogic.gdx.utils.Scaling
import com.badlogic.gdx.utils.viewport.ExtendViewport
import com.github.quillraven.fleks.World
import com.github.quillraven.fleks.world
import com.slo0ey.farmland.component.ImageComponent
import com.slo0ey.farmland.system.RenderSystem
import ktx.app.KtxScreen
import ktx.log.logger

class GameScreen: KtxScreen {
    private val stage: Stage = Stage(ExtendViewport(16f, 9f))
    private val playerTexture: Texture = Texture("image/entity/player.png")
    private val world: World = world {
        injectables {
            add("stage", stage)
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
            add(RenderSystem())
        }
    }

    override fun show() {
        LOG.debug { "GameScreen: show!" }

        world.entity {
            it += ImageComponent().apply {
                image = Image(TextureRegion(playerTexture, 0, 0, 64, 64)).apply {
                    setSize(4f, 4f)
//                    setScaling(Scaling.fill)
                }
            }
        }
        world.entity {
            it += ImageComponent().apply {
                image = Image(TextureRegion(playerTexture, 128, 64, 64, 64)).apply {
                    setPosition(0f, 4f)
                    setSize(4f, 4f)
//                    setScaling(Scaling.fill)
                }
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
        playerTexture.dispose()
        world.dispose()
    }

    companion object {
        private val LOG = logger<GameScreen>()
    }
}
