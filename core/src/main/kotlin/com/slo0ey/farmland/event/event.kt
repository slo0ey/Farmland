package com.slo0ey.farmland.event

import com.badlogic.gdx.maps.tiled.TiledMap
import com.badlogic.gdx.scenes.scene2d.Event

data class MapUpdateEvent(val map: TiledMap): Event()
