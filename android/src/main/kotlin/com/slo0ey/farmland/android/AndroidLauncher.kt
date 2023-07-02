package com.slo0ey.farmland.android

import android.os.Bundle

import com.badlogic.gdx.backends.android.AndroidApplication
import com.badlogic.gdx.backends.android.AndroidApplicationConfiguration
import com.slo0ey.farmland.Farmland

/** Launches the Android application. */
class AndroidLauncher : AndroidApplication() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        initialize(Farmland(), AndroidApplicationConfiguration().apply {
            // Configure your application here.
            useImmersiveMode = true // Recommended, but not required.
        })
    }
}
