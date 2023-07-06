package com.slo0ey.farmland

import com.badlogic.gdx.Application
import com.badlogic.gdx.Gdx
import com.slo0ey.farmland.screen.GameScreen
import ktx.app.KtxGame
import ktx.app.KtxScreen

class Farmland : KtxGame<KtxScreen>() {
    override fun create() {
        Gdx.app.logLevel = Application.LOG_DEBUG
        addScreen(GameScreen())
        setScreen<GameScreen>()
    }
}
