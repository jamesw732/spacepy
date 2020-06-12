#!/usr/bin/env python

from datamanager_rebin_common import *

times = numpy.arange(0., 7200, 300)
alpha = pa(numpy.arange(8).reshape(1, -1), times.reshape(-1, 1))
energies = numpy.logspace(0, 3, 10)
flux = j(numpy.reshape(energies, (1, 1, -1)),
                     numpy.reshape(times, (-1, 1, 1)),
                     numpy.expand_dims(alpha, -1))
pa_bins = numpy.arange(0, 181, 36)
flux_by_pa = spacepy.datamanager.rebin(
    flux, alpha, pa_bins, axis=1)
matplotlib.pyplot.pcolormesh(
    spacepy.toolbox.bin_center_to_edges(times), energies,
    flux_by_pa[:, 2, :].transpose(),
    norm=matplotlib.colors.LogNorm())
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.ylabel('Energy (MeV)')
matplotlib.pyplot.xlabel('Time (sec)')
matplotlib.pyplot.title('Flux at 90 degrees')
matplotlib.pyplot.show()
